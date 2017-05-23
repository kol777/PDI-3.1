# PDI-3.1

Application profiling based on machine learning tecniques.

As part of a Big Data platform, the students will extend the current work of an application that provisions services
in a Hadoop cluster based on the current and forecasted utilization. The objective of the work is to use machine learning techniques 
to profile and predict future application usages.

OS: Centos 7.2

Input: CSV files > 100MB

In the first phase, we've created a csv parser which goes through all the information from a csv and writes it in a text file (input).
We've implemented a mapper script which is only appending a "1" after every element from our input file and finally, the reducer which is using the output from the mapper script to count the appearences of the words.

*time cat input.txt | python mapper.py | sort -k 1,1 | python reducer.py*

real    1m50.789s

user    1m45.765s

sys    0m21.681s

In the next step we've installed hadoop 2.8.0 and all its dependencies and we ran our script using the hadoop jar:

*time sudo /opt/hadoop-2.8.0/bin/hadoop jar /opt/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -file /home/flavius/Desktop/mapper.py /home/flavius/Desktop/reducer.py -mapper 'python /home/flavius/Desktop/mapper.py' -reducer 'python /home/flavius/Desktop/reducer.py' -input /home/flavius/PDIII/input.txt -output /home/flavius/PDIII/output4*

By using top we noticed that the memory and CPU utilization had increased in a considerable manner.

After this we've installed an ambari-server, created a hadoop cluster and installed most of the ambari services.

Job.sh script can be used in crontab and the script will run a hadoop job with our mapreduce functions and it will save the memory and CPU utilization given by top in a metrics.txt file.


TODO:

Create a Job in Ambari (mapreduce service)

See metrics in Ambari (ambari-metrics service)

By seeing the metrics in Ambari, we will have a better understanding of how the application is behaving. Using the metrics from the ambari-metrics service, we will try to profile and predict future application usages with Machine Learning Techniques.
