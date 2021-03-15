#!/bin/sh

# Constants
PASSES=20000
HOST=localhost:3000
CAL=calibrate
PRO=process
PERF=./ApacheBench-prefix/src/ApacheBench-build/bin/runPerf.sh

$PERF -n $PASSES -s 'python ../process.py' -c $CAL -p $PRO -h $HOST
