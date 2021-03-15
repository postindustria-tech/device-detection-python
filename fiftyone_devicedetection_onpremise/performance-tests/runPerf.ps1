$scriptRoot = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition

# Constants
$PASSES=20000
$SERVICEHOST="localhost:5000"
$CAL="calibrate"
$PRO="process"
$PERF="$scriptRoot/ApacheBench-prefix/src/ApacheBench-build/bin/runPerf.ps1"

Invoke-Expression "$PERF -n $PASSES -s 'python ../process.py' -c $CAL -p $PRO -h $SERVICEHOST"


