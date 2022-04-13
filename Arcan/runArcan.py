import os
import time
import datetime

arcan_jar_path =" D:\JAVA\Arcan\\arcan-astracker\Arcan-1.4.0\Arcan-1.4.0-SNAPSHOT.jar "
project_name = "apache-openjpa"
java_project_path = " D:\JAVA\Java_Project\project1\\"+project_name
output_path = "D:\Java\Arcan\\arcan-astracker\\arcan_output\\"+project_name+"\\"
file = output_path+"graph-unversioned.graphml"
strs ="java -jar"+arcan_jar_path+" -p "+java_project_path+" -out "+ output_path
command = "start powershell.exe cmd /k "+strs
# command = "start cmd.exe cmd /k "+strs
time_path = project_name+".txt"

if os.path.exists(file) :
    os.remove(file);
start_time = datetime.datetime.now()
start = start_time.strftime('%Y-%m-%d %H:%M:%S.%f')
print("Start testing time: " + start + "\n")

os.system(command)

while 1<2:
    file = output_path + "graph-unversioned.graphml"
    if os.path.exists(file) :
        break;
end_time = datetime.datetime.now()
end = end_time.strftime('%Y-%m-%d %H:%M:%S.%f')
print("End testing time:" + end + "\n")
need_time = end_time - start_time
print("need time = " + str(need_time) + "\n")

with open(time_path, 'w') as f:
    f.write(project_name+ '\n')
    f.write("start = " + start + "\tend = " + end + "\tneed = " + str(need_time) + '\n')