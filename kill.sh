#!/bin/bash

# find the pid of rpizza.py
pid=$(ps -ef | grep "python rpizza.py" | grep -v grep | awk '{print $2}')

# make sure process was found
if [ -z "$pid" ]
then
    echo "process for RPIzza not found, exiting without taking any action"
    exit 1
fi

# kill the process with SIGTERM
kill -SIGTERM $pid

# check return value of kill command
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "kill command failed with exit code $retVal"
    exit $retVal
fi

echo "successfully killed RPIzza process"
exit 0
 

