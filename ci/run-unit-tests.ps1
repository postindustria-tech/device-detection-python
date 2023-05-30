param (
    [Parameter(Mandatory=$true)]
    [string]$RepoName
)

$packages = "fiftyone_devicedetection_onpremise"
./python/run-integration-tests.ps1 -RepoName $RepoName -Packages $packages

exit $LASTEXITCODE
