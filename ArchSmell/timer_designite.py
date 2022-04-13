import json
import os
import subprocess
import datetime
import time
import argparse


# path_to_repo 项目路径,
# path_to_output 输出路径
def timer_designite(path_to_repo, path_to_output):
    print('Timer start...')

    time_start = time.time()

    # 执行cmd命令
    logs = subprocess.run(['java','-Xmx4096m', '-jar', 'DesigniteJava.jar', '-i', path_to_repo, '-o', path_to_output], cwd='./',
        stdout=subprocess.PIPE)

    time_end = time.time()
    print("=============tool's log start=============")
    logs = logs.stdout.decode('ascii')
    # for log in logs:
    print(logs)
    print('=================log end=================')

    print('Timer end.')
    print('totally cost', time_end - time_start, 's.')

    return time_end - time_start


def main():
    parser = argparse.ArgumentParser(description="""Calculate the execution time of DesigniteJava.
                                                     """)
    parser.add_argument('--repo', type=str)
    parser.add_argument('--runtime', type=str)

    args = parser.parse_args()
    path_to_repo = args.repo
    path_to_output = args.output
    timer_designite(path_to_repo, path_to_output)

# 计算文件夹下的全部项目并保存到
def timer_designite_folder(folder_to_repo, folder_to_output):
    project_cost = {}

    for filename in os.listdir(folder_to_repo):
        # continue
        # with open(folder_to_repo + '/' + filename, encoding='UTF-8') as f:
        print(folder_to_repo + '\\' + filename)
        if filename not in ['camel', 'hive', 'hbase']:
            continue
        # continue
        path_to_repo = folder_to_repo + '\\' + filename
        path_to_output = folder_to_output + '\\' + filename

        cost = timer_designite(path_to_repo, path_to_output)
        project_cost[filename] = cost
        os.makedirs(folder_to_output, exist_ok=True)
        with open(folder_to_output + "\\{}_cost_time.json".format(filename), "w+") as jsonFile:
            jsonFile.write(json.dumps(project_cost))
        with open(folder_to_output + "\\{}_cost_time.txt".format(filename), "w+") as jsonFile:
            jsonFile.write(str(project_cost))
        # break
    os.makedirs(folder_to_output, exist_ok=True)
    # with open(folder_to_output + "\\project_cost_time.json", "w+") as jsonFile:
    #     jsonFile.write(json.dumps(project_cost))
    # with open(folder_to_output + "\\project_cost_time.txt", "w+") as jsonFile:
    #     jsonFile.write(str(project_cost))



if __name__ == '__main__':
    # path_to_repo = "F:\研究生生活\青岛软件所\开源软件供应链\项目进展\\arch smell\dataset\\abdera"
    # path_to_output = "F:\研究生生活\青岛软件所\开源软件供应链\项目进展\\arch smell\runtime\\abdera"
    # timer_designite(path_to_repo, path_to_output)

    '''
    example:
        python .\timer_designite.py --repo "F:\\研究生生活\\青岛软件所\\开源软件供应链\\项目进展\\arch smell\\dataset\\abdera" --runtime "F:\\研究生生活\\青岛软件所\\开源软件供应链\\项目进展\\arch smell\\runtime\\abdera"
    '''
    # main()
    # folder_to_repo = "F:\\研究生生活\\青岛软件所\\开源软件供应链\\项目进展\\arch smell\\dataset\\"
    # folder_to_output = "F:\\研究生生活\\青岛软件所\\开源软件供应链\\项目进展\\arch smell\\runtime\\designate\\"
    # timer_designite_folder(folder_to_repo, folder_to_output)
    folder_to_repo = "E:\\opensource\\仓库\\"
    folder_to_output = "F:\\研究生生活\\青岛软件所\\开源软件供应链\\项目进展\\arch smell\\runtime\\designate\\仓库\\"
    timer_designite_folder(folder_to_repo, folder_to_output)







