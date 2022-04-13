#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   recall.py
@Contact :   1213271050@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/6 12:30   gcx      1.0         None
'''

import datetime
import json
import csv
import os
import subprocess
import re
'''
输入正确集和测试集，输出测试集点覆盖率和边覆盖率
'''
def readCSV(filename,col_ca,firstLine = False):
    """
    输入：csv文件名，csv中记录修改的文件的列 表格默认为无title
    输出：修改过的文件列表
    :param filename:
    :param col_ca:
    :param firstLine = False
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
                components_affected = row[col_ca] # 数据直接读入即可
                print(components_affected)
                changed_files.append(components_affected)
    return set(changed_files)  # 进行去重


def readCSV_hotspot(filename,col_ca,firstLine = False):
    """
    输入：csv文件名，csv中记录修改的文件的列 表格默认为无title 把分隔符.替换成/
    输出：修改过的文件列表
    :param filename:
    :param col_ca:
    :param firstLine = False
    :return: changed_files
    """
    print("---------------------readCSVhotspot---------------------")
    changed_files = []
    with open(filename,'r',encoding="UTF-8") as f:
        read = csv.reader(f)
        for row in read:
            if firstLine:
                firstLine = False
                pass
            else:
                components_affected = row[col_ca] # hotspot的数据直接读入即可
                # components_affected = row[col_ca].split("$")[0].replace(".", "/")+".java" #arcan 取$前的子串，把.替换成/，加上后缀.java
                print(components_affected)
                changed_files.append(components_affected)
    return set(changed_files)  # 进行去重


def readCSV_arcan(filename,col_ca,col_type,firstLine = False):
    """
    输入：csv文件名，csv中记录修改的文件的列 记录csv列数据类型的列 表格默认为无title 把分隔符.替换成/ 把package种类筛掉 保留class类
    输出：修改过的文件列表
    :param filename:
    :param col_ca:
    :param col_type:记录csv列数据类型的列
    :param firstLine = False
    :return: changed_files
    """
    print("---------------------readCSVarcan---------------------")
    changed_files = []
    with open(filename,'r',encoding="UTF-8") as f:
        read = csv.reader(f)
        for row in read:
            if firstLine:
                firstLine = False
                pass
            else:
                if row[col_type] == "class":
                    # components_affected = row[col_ca] # hotspot的数据直接读入即可
                    pre = "src/java/" #前缀
                    suf = ".java" #后缀
                    components_affected = pre + row[col_ca].split("$")[0].replace(".", "/")+ suf #arcan 取$前的子串，把.替换成/，加上后缀.java
                    print(components_affected)
                    changed_files.append(components_affected)
    return set(changed_files)  # 进行去重

def readCSV_duc(filename,col_ca,firstLine = False):
    """
    输入：csv文件名，csv中记录修改的文件的列 记录csv列数据类型的列 表格默认为无title 把分隔符.替换成/
    输出：修改过的文件列表
    :param filename:
    :param col_ca:
    :param firstLine = False
    :return: changed_files
    """
    print("---------------------readCSVduc---------------------")
    changed_files = []
    with open(filename,'r',encoding="UTF-8") as f:
        read = csv.reader(f)
        for row in read:
            if firstLine:
                firstLine = False
                pass
            else:
                # components_affected = row[col_ca] # hotspot的数据直接读入即可
                suf = ".java" #后缀
                components_affected = row[col_ca].split("$")[0].replace(".", "/")+ suf #arcan 取$前的子串，把.替换成/，加上后缀.java
                print(components_affected)
                changed_files.append(components_affected)
    return set(changed_files)  # 进行去重


def readJson(filename):
    """
    输入：json文件名
    输出：json文件保存的边集edges和点集vertexes
    :param filename:
    :return: vertexes,edges
    """
    print("---------------------readJson---------------------")
    with open(filename,'r',encoding="UTF-8") as f:
        dic = json.load(f)
        # print(dic)
        vertexes = dic["vertexes"]
        edges = dic["edges"]
    return vertexes,edges

def recall(vertexes,edges,changed_files):
    """
    输入：正确集边集edges,正确集点集vertexes,测试集点集changed_files
    输出：边集合召回率
    :param vertexes：
    :param edges：
    :param changed_files：
    :return: 边集合召回率,点集合召回率,点准确率
    """
    print("---------------------recall---------------------")
    TP_vertexes = []
    TP_edges = []
    for node in changed_files:
        if node in vertexes:
            TP_vertexes.append(node)
    for edge in edges:
        # node1 = list(vertexes.keys())[list(vertexes.values()).index(edge[0])]
        # node2 = list(vertexes.keys())[list(vertexes.values()).index(edge[1])]
        node1 = vertexes[edge[0]]
        node2 = vertexes[edge[1]]
        if node1 in changed_files and node2 in changed_files : # 这里需要去重
            if [node1,node2] not in TP_edges and [node2,node1] not in TP_edges : #去重后添加
                TP_edges.append([node1,node2])

    recall_vertexes = float(len(TP_vertexes))/float(len(vertexes))
    recall_edges = float(len(TP_edges))/float(len(edges))
    pre_vertexes = float(len(TP_vertexes))/float(len(changed_files))
    return recall_vertexes,recall_edges, pre_vertexes

def depends(project_path,project_name):
    """
    用depends工具生成项目的依赖关系，以json的格式保存
    输入：
    project_path:项目的位置
    project_name:项目名字
    输出：
    basepath：depends工具生成的前缀地址 # 仅仅是把project_path中的/替换成\\
    json_file_path:生成的json文件保存项目的依赖关系
    """
    print("---------------------depends---------------------")

    basepath = "D:\\JAVA\\Arcan\\caffe\\"  # depends工具生成的前缀地址
    depends_jar_path = "D:/Python/ArchSmell/ArchSmell/depends-0.9.6/depends.jar" #depends_jar_path:depends工具的位置
    language = "python" #language:按照java/python/c等机器语言分析项目的依赖
    json_filename = project_name+"_depends"
    json_path_pre = "D:/Python/ArchSmell/CorrectDataSet/"
    json_file_path = json_path_pre + json_filename + ".json"
    logs = subprocess.run(['java', '-jar', depends_jar_path, language, project_path, json_filename],
                          cwd=json_path_pre,
                          stdout=subprocess.PIPE)

def run_hotspot(csv_filename,col_ca,CorrectDataSet):
    print("---------------------run---------------------")
    changed_files = readCSV_hotspot(csv_filename,col_ca,True) # 有title就传入参数True
    vertexes,edges = readJson(CorrectDataSet)
    vertexes_recall, edges_recall,vertexes_pre = recall(vertexes, edges, changed_files)
    print("vertexes_recall: " ,vertexes_recall)
    print("edges_recall: " ,edges_recall)
    print("vertexes_pre: ", vertexes_pre)
    return vertexes_recall,edges_recall,vertexes_pre

def run_arcan(csv_filename,col_ca,col_type,CorrectDataSet):
    print("---------------------run---------------------")
    changed_files = readCSV_arcan(csv_filename, col_ca,col_type,True)  # 有title就传入参数True
    vertexes,edges = readJson(CorrectDataSet)
    vertexes_recall, edges_recall,vertexes_pre = recall(vertexes, edges, changed_files)
    print("vertexes_recall: " ,vertexes_recall)
    print("edges_recall: " ,edges_recall)
    print("vertexes_pre: ", vertexes_pre)
    return vertexes_recall,edges_recall,vertexes_pre

def run_duc(csv_filename,col_ca,CorrectDataSet):
    print("---------------------run---------------------")
    changed_files = readCSV_duc(csv_filename, col_ca,True)  # 有title就传入参数True
    vertexes,edges = readJson(CorrectDataSet)
    vertexes_recall, edges_recall, vertexes_pre = recall(vertexes, edges, changed_files)
    print("vertexes_recall: ", vertexes_recall)
    print("edges_recall: ", edges_recall)
    print("vertexes_pre: ", vertexes_pre)
    return vertexes_recall, edges_recall, vertexes_pre


def test_duc(project_name):
    ###############################################################
    '''
    run duc recall
    :param project_name:
    :return:
    '''

    csv_filename = r"D:/Python/ArchSmell/CorrectDataSet/testdata/duc/"+project_name+".csv"  # 测试集的ArchSmell数据
    col_ca = 0  # 测试集archsmell的类的列
    CorrectDataSet = "D:/Python/ArchSmell/CorrectDataSet/correctdataset/"+project_name+"-original.json" # 正确集的路径
    vertexes_recall, edges_recall,vertexes_pre = run_duc(csv_filename, col_ca, CorrectDataSet)
    ###############################################################
    '''
    输出到文件中
    '''

    output_path = "D:/Python/ArchSmell/CorrectDataSet/output/duc/" + project_name + ".txt"

    with open(output_path, 'w') as f:
        f.write(project_name + ' run in duc\n')
        print("vertexes_recall: ", vertexes_recall, file=f)
        print("edges_recall: ", edges_recall, file=f)
        print("vertexes_pre: ",vertexes_pre,file = f)
        print("vertexes_f1: ", 2 * vertexes_recall * vertexes_pre / (vertexes_recall + vertexes_pre), file=f)

def test_hotspot(project_name):
    ###############################################################
    '''
    run hotspot recall
    :param project_name:
    :return:
    '''

    csv_filename = r"D:/Python/ArchSmell/CorrectDataSet/testdata/hotspot/"+project_name+".csv" #测试集的ArchSmell数据
    col_ca = 0 # 测试集archsmell的类的列
    CorrectDataSet = "D:/Python/ArchSmell/CorrectDataSet/correctdataset/"+project_name+"-original.json"#正确集的路径
    vertexes_recall,edges_recall,vertexes_pre = run_hotspot(csv_filename,col_ca,CorrectDataSet)
    ###############################################################
    '''
    输出到文件中
    '''

    output_path = "D:/Python/ArchSmell/CorrectDataSet/output/hotspot/" + project_name + ".txt"

    with open(output_path, 'w') as f:
        f.write(project_name + ' run in hotspot\n')
        print("vertexes_recall: ", vertexes_recall, file=f)
        print("edges_recall: ", edges_recall, file=f)
        print("vertexes_pre: ", vertexes_pre, file=f)
        print("vertexes_f1: ",2*vertexes_recall*vertexes_pre/(vertexes_recall+vertexes_pre),file=f)

def test_arcan(project_name):
    ##############################################################

    '''
    run arcan recall
    :param project_name:
    :return:
    '''

    csv_filename = r"D:/Python/ArchSmell/CorrectDataSet/testdata/arcan/"+project_name+".csv" #测试集的ArchSmell数据
    col_ca = 0 # 测试集archsmell的类的列
    col_type = 1
    CorrectDataSet = "D:/Python/ArchSmell/CorrectDataSet/correctdataset/"+project_name+"-withoutOrg.json"#正确集的路径
    vertexes_recall,edges_recall,vertexes_pre = run(csv_filename,col_ca,CorrectDataSet)
    ##############################################################
    '''
        输出到文件中
    '''

    output_path = "D:/Python/ArchSmell/CorrectDataSet/output/arcan/" + project_name + ".txt"

    with open(output_path, 'w') as f:
        f.write(project_name + ' run in arcan\n')
        print("vertexes_recall: ", vertexes_recall, file=f)
        print("edges_recall: ", edges_recall, file=f)
        print("vertexes_pre: ", vertexes_pre, file=f)
        print("vertexes_f1: ", 2 * vertexes_recall * vertexes_pre / (vertexes_recall + vertexes_pre), file=f)

def test_designate(project_name):
    ##############################################################
    '''
    run  designate recall
    :param project_name:
    :return:
    '''

    csv_filename = r"D:/Python/ArchSmell/CorrectDataSet/testdata/designate/"+project_name+".csv"  # 测试集的ArchSmell数据
    col_ca = 0  # 测试集archsmell的类的列
    CorrectDataSet = "D:/Python/ArchSmell/CorrectDataSet/correctdataset/"+project_name+"-withoutOrg.json"  # 正确集的路径
    vertexes_recall, edges_recall ,vertexes_pre= run(csv_filename, col_ca, CorrectDataSet)
    ##############################################################
    '''
        输出到文件中
    '''


    output_path = "D:/Python/ArchSmell/CorrectDataSet/output/designate/" + project_name + ".txt"

    with open(output_path, 'w') as f:
        f.write(project_name + ' run in designate\n')
        print("vertexes_recall: ", vertexes_recall, file=f)
        print("edges_recall: ", edges_recall, file=f)
        print("vertexes_pre: ", vertexes_pre, file=f)
        print("vertexes_f1: ", 2 * vertexes_recall * vertexes_pre / (vertexes_recall + vertexes_pre), file=f)


def setCSVFormate_arcan(csv_filename,firstLine = False):
    '''
    跑一次就够了
    修改为正确的格式
    :param csv_filename:
    :param firstLine:
    :return:
    '''
    headers = ['name', 'type', 'version', 'versionIndex', 'numOfClassesInPackage', 'linesOfCode', 'freqOfChanges', 'percCommitsClassChanged', 'changeHasOccurredMetric', 'percCommitsPackChanged', 'totalAmountOfChanges']
    data = []
    with open(csv_filename,'r',encoding="UTF-8") as f:
        read = csv.DictReader(f)
        for row in read:
            if row['type'] == "class":
                suf = ".java" #后缀
                components_affected = row['name'].split("$")[0].replace(".", "/")+suf #arcan 取$前的子串，把.替换成/，加上后缀.java
                # print(components_affected)
                row['name'] = components_affected
                data.append(row)
    with open(csv_filename, 'w', encoding="UTF-8",newline='') as f1:
        writer = csv.DictWriter(f1,headers)
        writer.writeheader()
        writer.writerows(data)

def run(csv_filename,col_ca,CorrectDataSet):
    print("---------------------run arcan/designate---------------------")
    # 从org开始
    changed_files = readCSV(csv_filename, col_ca,True)  # 有title就传入参数True
    vertexes,edges = readJson(CorrectDataSet) #输入特殊版以org开头的正确集
    vertexes_recall, edges_recall,vertexes_pre = recall(vertexes, edges, changed_files)
    print("vertexes_recall: " ,vertexes_recall)
    print("edges_recall: " ,edges_recall)
    print("vertexes_pre: ", vertexes_pre)
    return vertexes_recall,edges_recall,vertexes_pre

def testonce():
##############################################################
    # 用来处理arcan原始数据的
    # 已经执行过了 不用执行了
    # csv_filename = "D:/Python/ArchSmell/CorrectDataSet/testdata/arcan/ant-ivy.csv"  # 测试集的ArchSmell数据
    # setCSVFormate_arcan(csv_filename, True)
    # csv_filename = "D:/Python/ArchSmell/CorrectDataSet/testdata/arcan/cassandra.csv" #测试集的ArchSmell数据
    # setCSVFormate_arcan(csv_filename,True)
    # csv_filename = "D:/Python/ArchSmell/CorrectDataSet/testdata/arcan/openjpa.csv"  # 测试集的ArchSmell数据
    # setCSVFormate_arcan(csv_filename, True)
    # csv_filename = "D:/Python/ArchSmell/CorrectDataSet/testdata/arcan/pdfbox.csv"  # 测试集的ArchSmell数据
    # setCSVFormate_arcan(csv_filename, True)
    csv_filename = "D:/Python/ArchSmell/CorrectDataSet/testdata/arcan/avro.csv"  # 测试集的ArchSmell数据
    setCSVFormate_arcan(csv_filename, True)




if __name__ == '__main__':


    start_time = datetime.datetime.now()
    start = start_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    print("Start time: " + start + "\n")

###############################################################


    # project_name = "caffe"
    # project_path = "D:/JAVA/Arcan/caffe"  # 项目的地址
    # print("run depends" + project_name)
    # depends(project_path, project_name)
    testonce()

###############################################################
    # project_name = "ant-ivy"
    # project_name = "avro"
    # project_name = "camel"
    project_name = "cassandra"
    # project_name = "hadoop-b"
    # project_name = "hadoop-r"
    # project_name = "hbase"
    # project_name = "openjpa"
    # project_name = "pdfbox"

    test_hotspot(project_name)
    test_duc(project_name)
    test_designate(project_name)
    test_arcan(project_name)


###############################################################

    end_time = datetime.datetime.now()
    end = end_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    print("End time:" + end + "\n")
    need_time = end_time - start_time
    print("need time = " + str(need_time) + "\n")