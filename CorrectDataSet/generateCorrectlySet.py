import datetime
import json
import csv
import os


def readJson(filename,basepath):
    """
    输入：json文件名，json中记录的文件名的无关目录部分
    输出：点集和边集，点集为列表和字典的形式
    :param filename:
    :param basepath:
    :return: vertexes,edges,variables
    """
    print("-----------------------readJson--------------------")
    vertexes = {}
    edges = []
    variables = []
    with open(filename,'r',encoding="UTF-8") as f:
        dic = json.load(f)
        for i in range(len(dic["variables"])):
            s = dic["variables"][i]
            s = s.replace(basepath,"")
            s = s.replace("\\","/")
            vertexes[s] = i
            variables.append(s)

        for cell in dic["cells"]:
            a = []
            a.append(int(cell["src"]))
            a.append(int(cell["dest"]))
            edges.append(a)
    return vertexes,edges,variables

def readCSV(project_name, filename, firstLine = False):
    """
    输入：项目名，csv文件名
        csv格式：第0列为项目名，第1列为修改的文件
    输出：修改过的文件列表
    :param project_name:
    :param filename:
    :param col_ca:
    :param col_nof:
    :return: changed_files
    """
    print("---------------------readCSV---------------------")
    changed_files = []
    with open(filename,'r',encoding="UTF-8") as f:
        read = csv.reader(f)
        for row in read:
            if firstLine:
                firstLine = False
                pass
            else:
                if ( row[0].lower() == project_name ):
                    changed_files.append(row[1])
    return changed_files

def readCSV_XieShengLongGroup(project_name, filename, col_ca, col_nof):
    """
    输入：项目名，csv文件名，csv中记录修改的文件的列，csv中记录修改文件数的列
    输出：修改过的文件列表
    :param project_name:
    :param filename:
    :param col_ca:
    :param col_nof:
    :return: changed_files
    """
    print("---------------------readCSV_XieShengLongGroup---------------------")
    changed_files = []
    with open(filename,'r',encoding="UTF-8") as f:
        read = csv.reader(f)
        firstLine = True
        for row in read:
            if firstLine:
                firstLine = False
                pass
            else:
                if ( row[0].lower() == project_name ):
                    components_affected = row[col_ca].split()
                    if ( len(components_affected) != int(row[col_nof]) ):
                        print("ERROR: nof = " + row[col_nof] + " ,\tcomponents_affected = " + row[col_ca])
                    for component in components_affected:
                        changed_files.append(component)
    return changed_files

def output(output_dir,project_name,changed_files,vertexes_old,edges_old,variables_old):
    """
    输入：输出路径，项目名称，readCSV输出的changed_files，readJson输出的点集和边集
    :param output_dir:
    :param changed_files:
    :param vertexes_old:
    :param edges_old:
    :param variables_old:
    :return:
    """
    print("--------------------output-------------------------")
    vertexes_new = []
    edges_new = []
    #将changed_files和vertexes_old取交集，保存在vertexes_unite中
    vertexes_unite = []
    for file in changed_files:
        if ( vertexes_old.__contains__(file)):
            if not vertexes_unite.__contains__(file):
                vertexes_unite.append(file)
    #查询是否有边将vertexes_unite中的两个点相连，若有则加入vertexes_new，并将这条边的下标更新到edges_new中
    for vertex in vertexes_unite:
        index_old = vertexes_old[vertex]
        for edge in edges_old:
            if ( edge[0] == index_old and vertexes_unite.__contains__(variables_old[edge[1]]) ):
                vertex_another = variables_old[edge[1]]
                if ( not vertexes_new.__contains__(vertex) ):
                    vertexes_new.append(vertex)
                if ( not vertexes_new.__contains__(vertex_another) ):
                    vertexes_new.append(vertex_another)
                index_new = vertexes_new.index(vertex)
                index_new_anotherone = vertexes_new.index(vertex_another)
                a = []
                a.append(index_new)
                a.append(index_new_anotherone)
                edges_new.append(a)
    #写入output文件
    with open(output_dir,'w') as f:
        # #下面这种方法输出不太好看
        # final = {"projectName" : project_name, "date" : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), "vertexes" : vertexes_new, "edges" : edges_new}
        # final = json.dumps(final,indent=2)
        # f.writelines(final)

        #下面这种方法输出太麻烦了
        indent = "  "
        f.writelines("{\n")
        f.writelines(indent + "\"projectName\" : \"" + project_name + "\",\n")
        f.writelines(indent + "\"date\" : \"" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "\",\n")
        f.writelines(indent + "\"vertexes\" : [\n")
        flag = False
        for vertex in vertexes_new:
            if (not flag ):
                f.writelines(indent + indent + "\"" + vertex + "\"")
                flag = True
            else:
                f.writelines(",\n"+indent + indent + "\"" + vertex + "\"")
        f.writelines("\n" + indent + "],\n")
        f.writelines(indent + "\"edges\" : [\n")
        flag = False
        for edge in edges_new:
            if ( not flag ):
                f.writelines(indent + indent + str(edge))
                flag = True
            else:
                f.writelines(",\n"+indent + indent + str(edge))
        f.writelines("\n" + indent + "]\n")
        f.writelines("}")


def test(output_dir,changed_files,vertexes_old,edges_old,variables_old):
    indexes = []
    indexes.append(vertexes_old["python/caffe/io.py"])
    indexes.append(vertexes_old["examples/pycaffe/layers/pascal_multilabel_datalayers.py"])
    indexes.append(vertexes_old["python/caffe/pycaffe.py"])
    indexes.append(vertexes_old["python/caffe/net_spec.py"])
    indexes.append(vertexes_old["tools/extra/extract_seconds.py"])
    indexes.append(vertexes_old["tools/extra/parse_log.py"])
    print(indexes)
    for index in indexes:
        print("index = " + str(index))
        for edge in edges_old:
            if ( edge[0] == index ):
                print(edge[1])
            if ( edge[1] == index ):
                print(edge[0])



if __name__ == '__main__':

    """
    修改以下参数：
    project_name    项目名称
    basepath        depends文件中路径的无关部分，用于将绝对路径改为相对路径
    json_filename   depends文件
    csv_filename    收集到的修改的文件，格式：第0列为项目名，第1列为带路径的文件名
    output_dir      输出文件
    """
    project_name = "caffe"
    basepath = "D:\\Desktop\\1\\depstest\\data\\caffe\\"
    json_filename = r"D:\Desktop\PyCharm-project\arch-smell\data\caffe-python.json"
    csv_filename = r"D:\Desktop\PyCharm-project\arch-smell\data\dataset-test-hasFirstline.csv"
    output_dir = "output\\" + project_name + ".json"

    vertexes,edges,variables = readJson(json_filename,basepath)
    changed_files = readCSV(project_name, csv_filename, firstLine=False)
    output(output_dir,project_name,changed_files,vertexes,edges,variables)