#!/bin/bash

file="serial_sorted.txt"

# Check if fetched_tweets textfile already exists, if so, remove it
if [ -f $file ] ; then
    rm $file
fi

# Run the python script with the command line argument
python3 serial-wordcount.py $1
