param (
    [Parameter(Mandatory=$true)]
    [string]$RepoName
)

if ($IsWindows) {
    # Shorten the temporary directory path to work around MSVC path lenght limit
    $env:TEMP = New-Item -ItemType Directory -Force -Path "C:\tmp"
    Write-Output $env:TEMP
}

$packages = "fiftyone_devicedetection_onpremise"
./python/run-unit-tests.ps1 -RepoName $RepoName -Packages $packages

exit $LASTEXITCODE
