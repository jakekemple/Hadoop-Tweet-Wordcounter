# hadoop-demo-project
## This repo contains a demonstration project to display the usefulness of Hadoop with Python.

## Based on http://www.glennklockwood.com/data-intensive/hadoop/streaming.html with 
some modifications to work on our Hadoop system.

### 1. Transfer Mapper and Reducer programs to server, along with any input files.
 - We used FileZilla, but any file transfer program should work
	
### 2. Log in to server.
 - run 'ssh [username]@[server]' and enter password as prompted
	
### 3: Copy the input files to Hadoop's filesystem (HDFS).
 - Commands to manipulate the HDFS begin with 'hdfs dfs', followed by the command to execute and any other arguments
 - Most HDFS commands are similar to the regular Linux/Unix commands you would
	 use (mkdir, ls, rm, etc.)
	
 -run 'hdfs dfs -mkdir [directory name]' to create a new directory
 -run 'hdfs dfs -copyFromLocal [file on local filesystem] [location on HDFS]' 
	 to copy the files onto HDFS
 -The hdfs commands seemed to work best with absolute paths, at least when
	 giving the HDFS location (for example, '/wordcount' rather than 'wordcount)
	 
 -Following the example from the website, we would type:
		hdfs dfs -mkdir /wordcount
		hdfs dfs -copyFromLocal ./pg2701.txt /wordcount/mobydick.txt
	
 -'hdfs dfs -ls [directory name]' can be used to verify the files were copied

### 4: Run the Hadoop job!
 - The basic command is:
		'hadoop jar [path to streaming file]
		- mapper [mapper executable]
		- reducer [reducer executable]
		- input [path to input file on HDFS]
		- output [folder on HDFS to place output data]'
 - On our system, the file we want to execute is 'hadoop-streaming-2.7.3.jar',
	 located in the folder '/usr/local/hadoop/share/hadoop/tools/lib'
	
 - Again following the website's example, we would run:
		hadoop \
		jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
		- mapper "python $PWD/mapper.py" \
		- reducer "python $PWD/reducer.py" \
		- input "/wordcount/mobydick.txt" \
		- output "/wordcount/output"
	
 - The mapper and reducer arguments should give the path to the programs on the 
	 local filesystem, while input and output are on the HDFS
 - $PWD gives the current working directory
 - Can type 'hadoop-streaming-*.jar' instead of remembering the exact version number
	
### 5: Getting the output.
 - Assuming the job completes successfully, the output will be placed in the
	 folder specified in the above command.
	 
 - run 'hdfs dfs -copyToLocal [HDFS output folder] .' to copy the folder to the
	 current directory on the regular filesystem.
 - Alternatively, use 'hdfs dfs -ls [HDFS output folder]' to examine the contents 
	 of the folder and then just copy the individual file(s)
	 
 - The output files are plain text files, and can be viewed with whatever 
	 text editors we have on the server