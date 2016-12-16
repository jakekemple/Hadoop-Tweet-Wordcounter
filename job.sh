#!/bin/bash

# Copy textfile to the hdfs job folder
hdfs dfs -copyFromLocal -f $1 /tweet-wordcounter-job

# Remove completed-wordcount directory from past completed jobs
hdfs dfs -rm -r -f /completed-wordcount

# MapReduce Job
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -mapper "python3 mapper.py" -reducer "python3 reducer.py" -input /tweet-wordcounter-job/$1 -output /completed-wordcount


# Check for local copy of completed-wordcount directory and remove
if [ -d "completed-wordcount" ]; then
    rm -rf "completed-wordcount"
fi

# Copy completed-wordcount directory to local directory
hdfs dfs -copyToLocal /completed-wordcount
