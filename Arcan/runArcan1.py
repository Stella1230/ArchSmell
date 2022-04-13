import os
import time
import datetime
import subprocess


'''
project_name = "hive"
java_project_path = "D:\JAVA\Java_Project\project1\hive\src\hive-0.3.0-hadoop-0.17.0-dev"

project_name = "cassandra"
java_project_path = "D:\JAVA\Java_Project\project1\\apache-cassandra\\apache-cassandra-0.5.1"

project_name = "hbase"
java_project_path = "D:\JAVA\Java_Project\project1\hbase\hbase-0.1.0"

project_name = "camel"
java_project_path = "D:\JAVA\Java_Project\project1\\apache-camel\\apache-camel-1.6.0"

project_name = "ant"
java_project_path = "D:\JAVA\Java_Project\project1\\apache-ant"

# ok
project_name = "ant"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\ant"

# ok
project_name = "cassandra"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\cassandra"

# ok
project_name = "hbase"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\hbase"

# camel源码有问题 java.lang.RuntimeException: Invalid package name $
project_name = "camel"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\camel"

# ok
project_name = "hdfs"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\hadoop-hdfs"

##java.lang.NullPointerException
project_name = "hive"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\hive"

#java.lang.IllegalStateException: Module should be known
project_name = "log4j2"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\logging-log4j2"

# ok
project_name = "openjpa"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\openjpa"

# ok
project_name = "zookeeper"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\zookeeper"

'''

project_name = "hdfs"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\hadoop-hdfs"

# project_name = "apache-openjpa"  # 改
# java_project_path = " D:/JAVA/Java_Project/project1/"+project_name  # 改

arcan_jar_path ="D:/JAVA/Arcan/arcan-astracker/Arcan-1.4.0/Arcan-1.4.0-SNAPSHOT.jar"
output_path_arcan = "D:/Java/Arcan/arcan-astracker/arcan_output/"+project_name+"/"
file = output_path_arcan+"graph-unversioned.graphml"
strs_arcan ="java -jar"+arcan_jar_path+" -p "+java_project_path+" -out "+ output_path_arcan
command = "start powershell.exe cmd /k "+strs_arcan
time_path = project_name+".txt"

start_time1 = datetime.datetime.now()
start1 = start_time1.strftime('%Y-%m-%d %H:%M:%S.%f')
print("Start testing time: " + start1 + "\n")

logs = subprocess.run(['java', '-jar', arcan_jar_path , '-p', java_project_path, '-out', output_path_arcan], cwd='./',
    stdout=subprocess.PIPE)
# logs = subprocess.run(['java', '-jar', arcan_jar_path , '-p', java_project_path, '-out','-git','-branch', output_path_arcan], cwd='./',
#     stdout=subprocess.PIPE)

end_time1 = datetime.datetime.now()
end1 = end_time1.strftime('%Y-%m-%d %H:%M:%S.%f')

print("End testing time:" + end1 + "\n")
need_time1 = end_time1 - start_time1
print("need time = " + str(need_time1) + "\n")


astracker_jar_path = "D:/JAVA/Arcan/arcan-astracker/astracker_old/target/astracker-0.9.0-jar-with-dependencies.jar"
output_path_astracker = "D:/JAVA/Arcan/arcan-astracker/astracker_output"
strs_astracker = "java -jar "+astracker_jar_path+" -p "+project_name+" -i "+output_path_arcan+" -out "+output_path_astracker+" -pC -pCC "



start_time2 = datetime.datetime.now()
start2 = start_time2.strftime('%Y-%m-%d %H:%M:%S.%f')
print("Start testing time: " + start2 + "\n")

# logs = subprocess.run(['java', '-jar', astracker_jar_path , '-p', project_name, '-i',output_path_arcan, '-o', output_path_astracker,'-pC','-pCC'], cwd='./',
#     stdout=subprocess.PIPE)

end_time2 = datetime.datetime.now()
end2 = end_time2.strftime('%Y-%m-%d %H:%M:%S.%f')

print("End testing time:" + end2 + "\n")
need_time2 = end_time2 - start_time2
print("need time = " + str(need_time2) + "\n")

with open(time_path, 'w') as f:
    f.write(project_name+ '\n')
    f.write("------------------------start in arcan------------------------\n")
    f.write("start = " + start1 + "\tend = " + end1 + "\tneed = " + str(need_time1) + '\n')
    f.write("------------------------start in astracker------------------------\n")
    f.write("start = " + start2 + "\tend = " + end2 + "\tneed = " + str(need_time2) + '\n')