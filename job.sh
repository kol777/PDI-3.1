#!/bin/bash
# This script is added in cron to get CPU and Memory metrics after a Hadoop Job, saving the output to a file called metrics.txt
# It can be run only as root

if [ "`id -u`" != '0' ]; then
  echo 'Error: you must be superuser.'
  exit 1
fi

/opt/hadoop-2.8.0/bin/hadoop jar /opt/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -file /home/flavius/Desktop/mapper.py /home/flavius/Desktop/reducer.py -mapper 'python /home/flavius/Desktop/mapper.py' -reducer 'python /home/flavius/Desktop/reducer.py' -input /home/flavius/PDIII/input.txt -output /home/flavius/PDIII/output4
top -b -n 5 | head -n 20  | tail -n 14 | awk '{print $9 "   " $10 "   " $12}' > /home/flavius/metrics.txt
