#!/bin/bash
time sudo /opt/hadoop-2.8.0/bin/hadoop jar /opt/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -file /home/flavius/Desktop/mapper.py /home/flavius/Desktop/reducer.py -mapper 'python /home/flavius/Desktop/mapper.py' -reducer 'python /home/flavius/Desktop/reducer.py' -input /home/flavius/PDIII/input.txt -output /home/flavius/PDIII/output4
top -b -n 5 | head -n 20  | tail -n 14 | awk '{print $9 "   " $10 "   " $12}' > metrics.txt
