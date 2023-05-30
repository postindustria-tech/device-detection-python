param (
    [Parameter(Mandatory=$true)]
    [string]$RepoName
)

$packages = "fiftyone_devicedetection_onpremise"
./python/run-unit-tests.ps1 -RepoName $RepoName -Packages $packages

exit $LASTEXITCODE
