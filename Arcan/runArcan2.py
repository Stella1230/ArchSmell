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

project_name = "ant"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\ant"

project_name = "cassandra"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\cassandra"

project_name = "hbase"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\hbase"

#camel源码有问题 java.lang.RuntimeException: Invalid package name $
project_name = "camel"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\camel"

project_name = "hdfs"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\hadoop-hdfs"

project_name = "hive"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\hive"

project_name = "log4j2"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\logging-log4j2"

project_name = "openjpa"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\openjpa"

project_name = "zookeeper"
java_project_path = "D:\JAVA\Java_Project\\remote_java\\zookeeper"

'''
def run(project_name,ava_project_path):
    # project_name = "cassandra"
    # java_project_path = "D:/JAVA/Java_Project/4.5八个项目/cassandra -b cassandra-1.0.7"
    # project_name = "apache-openjpa"  # 改
    # java_project_path = " D:/JAVA/Java_Project/project1/"+project_name  # 改

    arcan_jar_path ="D:/JAVA/Arcan/arcan-astracker/Arcan-1.4.0/Arcan-1.4.0-SNAPSHOT.jar"
    # arcan_jar_path ="D:/JAVA/Arcan/arcan-astracker/Arcan-c-1.3.1-SNAPSHOT-jar-with-dependencies.jar"
    output_path_arcan = "D:/Java/Arcan/arcan-astracker/arcan_output/"+project_name+"/"
    # file = output_path_arcan+"graph-unversioned.graphml"
    file = output_path_arcan+"graph-1.graphml"
    strs_arcan ="java -jar"+arcan_jar_path+" -p "+java_project_path+" -out "+ output_path_arcan
    command = "start powershell.exe cmd /k "+strs_arcan


    start_time1 = datetime.datetime.now()
    start1 = start_time1.strftime('%Y-%m-%d %H:%M:%S.%f')
    print("Start testing time: " + start1 + "\n")

    logs = subprocess.run(['java', '-jar', arcan_jar_path , '-p', java_project_path, '-out', output_path_arcan], cwd='D:/Python/ArchSmell/Arcan/',
        stdout=subprocess.PIPE)

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

    logs = subprocess.run(['java', '-jar', astracker_jar_path , '-p', project_name, '-i',output_path_arcan, '-o', output_path_astracker,'-pC','-pCC'], cwd='./',
        stdout=subprocess.PIPE)

    end_time2 = datetime.datetime.now()
    end2 = end_time2.strftime('%Y-%m-%d %H:%M:%S.%f')

    print("End testing time:" + end2 + "\n")
    need_time2 = end_time2 - start_time2
    print("need time = " + str(need_time2) + "\n")

    time_path = output_path_astracker+"/trackASOutput/"+project_name+"/" + project_name + "_runtime.txt"

    with open(time_path, 'w') as f:
        f.write(project_name+ '\n')
        f.write("------------------------start in arcan------------------------\n")
        f.write("start = " + start1 + "\tend = " + end1 + "\tneed = " + str(need_time1) + '\n')
        f.write("------------------------start in astracker------------------------\n")
        f.write("start = " + start2 + "\tend = " + end2 + "\tneed = " + str(need_time2) + '\n')

if __name__ == '__main__':
    # #####1######
    # project_name = "ant"
    # print(project_name)
    # java_project_path = "D:\JAVA\Java_Project\project4.5\\ant-ivy -b 2.3.0"
    # run(project_name,java_project_path)
    # # #####1######
    # ######2######
    # #java.lang.RuntimeException: Invalid package name $
    # project_name = "avro"
    # print(project_name)
    # 注释了archetypes里的一些文件
    # .\archetypes\avro-service-archetype\src\main\resources\archetype-resources\src\main和...\test里的java文件
    # java_project_path = "D:\JAVA\Java_Project\project4.5\\avro -b release-1.7.6\lang\java\\avro"
    # # java_project_path = "D:\JAVA\Java_Project\project4.5\\avro -b release-1.7.6\lang\java\ipc"
    # # java_project_path = "D:\JAVA\Java_Project\project4.5\\avro -b release-1.7.6\lang\java\mapred"
    # # java_project_path = "D:\JAVA\Java_Project\project4.5\\avro -b release-1.7.6\lang\java\compiler"
    # java_project_path = "D:\JAVA\Java_Project\project4.5\\avro -b release-1.7.6\lang\java\protobuf"
    # java_project_path = "D:\JAVA\Java_Project\project4.5\\avro -b release-1.7.6\lang\java\\thrift"
    # java_project_path = "D:\JAVA\Java_Project\project4.5\\avro -b release-1.7.6\lang\java\\tools"
    # java_project_path = "D:\JAVA\Java_Project\project4.5\\avro -b release-1.7.6\lang\java\\trevni"
    # java_project_path = "D:\JAVA\Java_Project\project4.5\\avro -b release-1.7.6\lang\java\\archetypes"
    # java_project_path = "D:\JAVA\Java_Project\project4.5\\avro -b release-1.7.6\lang\java"
    # run(project_name,java_project_path)
    ######2######
    ######3######
    # # java.lang.RuntimeException: Invalid package name $
    # project_name = "camel"
    # print(project_name)
    # java_project_path = "D:/JAVA/Java_Project/project4.5/camel -b camel-2.11.1"
    # # java_project_path = "D:/JAVA/Java_Project/project4.5/camel -b camel-2.11.1/tooling"
    # run(project_name,java_project_path)
    ######3######
    #####4######
    project_name = "cassandra"
    print(project_name)
    java_project_path = "D:/JAVA/Java_Project/project4.5/cassandra -b cassandra-1.0.7"
    run(project_name,java_project_path)
    ####4######
    # ######5######
    # #java.lang.NullPointerException: Cannot read field "fPackage" because "typeDeclaration.binding" is null
    # project_name = "hadoop-branch-2.2.0"
    # print(project_name)
    # java_project_path = "D:/JAVA/Java_Project/project4.5/hadoop -b branch-2.2.0"
    # run(project_name,java_project_path)
    # ######5######
    # ######6######
    # #java.lang.NullPointerException: Cannot read field "compoundName" because "type.binding" is null
    # project_name = "hadoop-release-2.2.0"
    # print(project_name)
    # java_project_path = "D:/JAVA/Java_Project/4.5八个项目/hadoop -b release-2.2.0"
    # run(project_name,java_project_path)
    # ######6######
    # ######7######
    # #java.lang.NullPointerException: Cannot invoke "spoon.reflect.reference.CtPackageReference.getSimpleName()" because the return value of
    # # "spoon.reflect.reference.CtTypeReference.getPackage()" is null
    # project_name = "hbase"
    # print(project_name)
    # java_project_path = "D:/JAVA/Java_Project/project4.5/hbase"
    # run(project_name, java_project_path)
    # ######7######
    # #####8######
    project_name = "openjpa"
    print(project_name)
    java_project_path = "D:/JAVA/Java_Project/project4.5/openjpa -b 2.2.2"
    run(project_name, java_project_path)
    #####8######
    #####9######
    project_name = "pdfbox"
    print(project_name)
    java_project_path = "D:/JAVA/Java_Project/project4.5/pdfbox -b 1.8.4"
    run(project_name, java_project_path)
    #####9######