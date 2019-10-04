# Hadoop Data Analysis

Permissions need to be granted to run the mapper and reducer files. 
And that can be done using the following command

chmod 755 mapper.py reducer.py


Input is located at /user/tatavag/nyc.data 


Command to execute the program on the Hadoop Server:

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file /home/malyalaa/mapper.py -mapper /home/malyalaa/mapper.py -file /home/malyalaa/reducer.py -reducer /home/malyalaa/reducer.py -input /user/tatavag/nyc.data -output /user/malyalaa/out


After the job is successfully done, it notifies the user by displaying the output directory

Output directory is /user/malyalaa/out
 

Command to list the files present in the output directory:

hadoop fs -ls /user/malyalaa/out


Output file is /user/malyalaa/out/part-00000


It can be displayed using the below command:

hdfs dfs -cat /user/malyalaa/out/part-00000


Also, the output can be copied into another text file using the below command:

hdfs dfs -cat /user/malyalaa/out/part-00000 >> hw4_out.txt
