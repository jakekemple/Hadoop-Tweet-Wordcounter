# Hadoop Tweet Wordcounter Job

## What is it?

A tweet retriever & hadoop wordcounter job. Built to show the hadoop hdfs usage for a CSC 333 profect at Missouri State University.

## Why use it?

For sentimental analysis of the most recent tweets containing a particular hashtag. For example, if you run the job on tweets containing the hashtag `#food`, you may be able to make conclusions about the most discussed meals within a given amount of time the tweets were retrieved. 

## How it works

There are 2 major steps in running the project: 
1. Retrieve tweets via twitter-api by hashtag and put them into a textfile
2. Run a wordcounter script with Hadoop to count the number of word occurences in the retrieved tweets file 

## Steps to setup & run:

1. Make sure you have hadoop 2.7.3 and python 3 installed on your server or local computer where you will be hosting the project.

2. Run the tweet retriever script with `./get-tweets.sh #hashtag-word`, where `#hashtag-word` is your desired hashtag. To quit the script after desired amount of tweets are retrieved, use 'Ctrl-C'. 

3. To copy the textfile to HDFS & run the hadoop job on the file, run `./job.sh [textfilename.txt]`. NOTE: The default textfile created from the tweet retriever in step 2 is 'fetched_tweets.txt', so this should be used unless you plan to use a different textfile in the hadoop wordcounter.
	
## Viewing the Output:

1. Assuming the job completes successfully, the output will be placed in the local folder where the repository files are located.
2. Open and view the textfile inside the '/completed-wordcount' directory. Words are sorted by most common occurences to least common occurences 
	 
### Notes:
- There is a serial wordcount script that can be used in lieu of the Hadoop job script. Run `python serial-wordcount.py [filename.txt]` instead of the job.sh script.
- Commands to manipulate the HDFS begin with `hdfs dfs`, followed by the command to execute with any other arguments
- `hdfs dfs -ls [directory name]` can be used to verify files were copied to the HDFS
- If you need to create a directory on the HDFS, run `hdfs dfs -mkdir /directory-name`
- You can type 'hadoop-streaming-*.jar' instead of remembering the exact version number when accessing the hadoop jar file
- $PWD gives the current working directory
	 
### External Resources & Documentation:
1. Mapper & Reducer based on this [Hadoop Application Walkthrough](http://www.glennklockwood.com/data-intensive/hadoop/streaming.html)
