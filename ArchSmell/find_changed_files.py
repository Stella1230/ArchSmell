import json

from git2log import git2log


# E:\opensource\ArchSmell\szz\results\fix_and_introducers_pairs.json
def load_commits(pairs_dir):
    commits = {}
    with open(pairs_dir, 'r') as f:
        s = f.read()
        paris = json.loads(s)
        for pair in paris:
            commits[pair[0]] = ''
            commits[pair[1]] = ''

    return commits



def get_commit_files(logs):
    commit_files = {}
    # 将日志文件转为commit::changed files的字典
    for log in logs:
        # print(log)
        commit_files[log['commit']] = log['changes']

    return commit_files

# 根据日志文件与commits数据，找出文件修改次数
def find_changed_files(logs, commits):
    # 记录文件修改次数
    num_file_changed = {}
    # 将日志文件转为commit::changed files的字典
    commit_files = get_commit_files(logs)
    # 获取全部文件修改次数
    for commit in commits:
        if commit in commit_files.keys():
            changed_files = commit_files[commit]
            for file in changed_files:
                filename = file[2]
                if filename in num_file_changed.keys():
                    num_file_changed[filename] += 1;
                else:
                    num_file_changed[filename] = 1;

    return num_file_changed


def filter_changed_files(num_file_changed, threshold):
    num_file_filtered = {}
    for file in num_file_changed.keys():
        if num_file_changed[file] >= threshold:
            num_file_filtered[file] = num_file_changed[file]

    return num_file_filtered


if __name__ == "__main__":

    git_dir = 'F:\\研究生生活\\青岛软件所\\开源软件供应链\项目进展\\arch smell\\dataset\\abdera\\.git'
    git_dir = 'E:\\opensource\\仓库\\logging-log4j2\\.git'
    s = git2log(git_dir)
    logs = json.loads(s)

    pairs_dir = 'E:\\opensource\\ArchSmell\\szz\\results\\fix_and_introducers_pairs.json'
    pairs_dir = 'E:\\opensource\\ArchSmell\\szz\\fix_and_introducers_pairs.json'
    commits = load_commits(pairs_dir)

    num_file_changed = find_changed_files(logs, commits)
    # 阈值过滤
    num_file_filtered = filter_changed_files(num_file_changed, threshold=5)

