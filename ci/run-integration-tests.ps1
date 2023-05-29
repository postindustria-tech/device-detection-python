param (
    [Parameter(Mandatory=$true)]
    [string]$RepoName,
    [Parameter(Mandatory=$true)]
    [Hashtable]$Keys
)

$packages = "fiftyone_devicedetection_cloud", "fiftyone_devicedetection_onpremise", "fiftyone_devicedetection_examples"
./python/run-integration-tests.ps1 -RepoName $RepoName -Packages $packages -Keys $Keys

exit $LASTEXITCODE
