#!/bin/bash

# Copy fetched_tweets textfile to the hdfs job folder
hdfs dfs -copyFromLocal -f fetched_tweets.txt /tweet-wordcounter-job

# Remove completed-wordcount directory from past completed jobs
hdfs dfs -rm -r -f /completed-wordcount

start=`date +%s`

# MapReduce Job
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -mapper "python3 mapper.py" -reducer "python3 reducer.py" -input /tweet-wordcounter-job/fetched_tweets.txt -output /completed-wordcount

end=`date +%s`

runtime=$((end-start))

# Check for local copy of completed-wordcount directory and remove
if [ -d "completed-wordcount" ]; then
    rm -rf "completed-wordcount"
fi

# Copy completed-wordcount directory to local directory
hdfs dfs -copyToLocal /completed-wordcount
