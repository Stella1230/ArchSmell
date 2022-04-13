import subprocess


def execute_cmd(cmd):
    # 执行cmd命令
    print('start...')
    logs = subprocess.run(cmd, cwd='E:\\opensource\\ArchSmell\\', stdout=subprocess.PIPE)
    # print("=============log start=============")
    # logs = logs.stdout.decode('ascii')
    # # for log in logs:
    # print(logs)
    # print('=================log end=================')
    print('down.')



"""

python git_log_to_array.py --from-commit 8090fe09b0d0426e365325887a1aa0981816fb1d --repo-path "F:\研究生生活\青岛软件所\开源软件供应链\项目进展\arch smell\dataset\abdera"
python fetch.py --issue-code HDFS --jira-project issues.apache.org/jira
python find_bug_fixes.py --gitlog gitlog.json --issue-list issues --gitlog-pattern "ABDERA-{nbr}\D|#{nbr}\D"
gitlog/{}/gitlog.json'.format(project_name)

java -jar ./szz_find_bug_introducers-0.1.jar -i ../issues_lists/hadoop-hdfs/issue_list.json -r "F:\研究生生活\青岛软件所\开源软件供应链\项目进展\arch smell\dataset\hadoop-hdfs"
java -jar ./szz_find_bug_introducers-0.1.jar -i ../issues_lists/logging-log4j2/issue_list.json -r "F:\研究生生活\青岛软件所\开源软件供应链\项目进展\arch smell\dataset\logging-log4j2"

"""
if __name__ == '__main__':
    # ABDERA
    commit_id = "8090fe09b0d0426e365325887a1aa0981816fb1d"
    repo_path = 'F:\\研究生生活\\青岛软件所\\开源软件供应链\\项目进展\\arch smell\\dataset\\abdera'
    issue_code = 'ABDERA'
    jira_project = 'issues.apache.org/jira'
    # HDFS
    commit_id = "b2d2a3262c587638db04c2991d48656b3d06275c"
    repo_path = 'F:\\研究生生活\\青岛软件所\\开源软件供应链\\项目进展\\arch smell\\dataset\\hadoop-hdfs'
    issue_code = 'HDFS'
    jira_project = 'issues.apache.org/jira'
    # ANT
    commit_id = "7ab122252c0c26284a8801e45785c5b1f4f6295f"
    repo_path = 'E:\\opensource\\仓库\\ant'
    issue_code = 'ANT'
    jira_project = 'issues.apache.org/jira'
    # CASSANDRA
    commit_id = "b9d9f9c7dab9b39fb27a4be0b6d9ce2a8718167e"
    repo_path = 'E:\\opensource\\仓库\\cassandra'
    issue_code = 'CASSANDRA'
    jira_project = 'issues.apache.org/jira'
    # LOG4J2
    commit_id = "a392a16688a788d615d1f0ac696c5f64e4ca32b1"
    repo_path = 'E:\\opensource\\仓库\\logging-log4j2'
    issue_code = 'LOG4J2'
    jira_project = 'issues.apache.org/jira'
    # LOG4J2
    commit_id = "a392a16688a788d615d1f0ac696c5f64e4ca32b1"
    repo_path = 'D:\\opensource\\仓库\\logging-log4j2'
    issue_code = 'LOG4J2'
    jira_project = 'issues.apache.org/jira'

    git_log_to_array = 'python git_log_to_array.py --from-commit {} --repo-path '.format(commit_id) + '\"' +  repo_path + '\"'

    fetch = 'python fetch.py --issue-code {} --jira-project {}'.format(issue_code, jira_project)

    project_name = repo_path.split('\\')[-1]
    gitlog = 'gitlog/{}/gitlog.json'.format(project_name)
    issue_list = 'issues/{}/'.format(issue_code)
    issue_list_output = 'issues_lists/{}/'.format(project_name)

    find_bug_fixes = 'python find_bug_fixes.py --gitlog {0} --issue-list {1} --gitlog-pattern \"{2}'.format(
        gitlog, issue_list, issue_code
    ) + '-{nbr}\D|#{nbr}\D\" ' + '--runtime \"{}\"'.format(issue_list_output)

    szz = 'java -jar ./szz_find_bug_introducers-0.1.jar -i ../issues_lists/{0}/issue_list.json -r \"{1}\"'.format(project_name, repo_path)

    print(git_log_to_array)
    print(fetch)
    print(find_bug_fixes)
    # 先进入szz文件夹，再运行
    print(szz)
    """
    java -jar ./szz_find_bug_introducers-0.1.jar -i ../issues_lists/logging-log4j2/issue_list.json -r "E:\opensource\仓库\logging-log4j2"
    """