param (
    [Parameter(Mandatory=$true)]
    [string]$RepoName,
    [Parameter(Mandatory=$true)]
    [Hashtable]$Keys
)

# nightly-publish-main workflow doesn't create the examples package, so
# install-package.ps1 won't install it and its test dependencies won't get
# installed. That's why we install it here, as a special case.
if ($env:GITHUB_JOB -eq "Test") {
    Write-Output "Installing 'fiftyone_devicedetection_examples' package to install its dependencies"
    pip install $RepoName/fiftyone_devicedetection_examples || $(throw "pip install failed")
}

$packages = "fiftyone_devicedetection_cloud", "fiftyone_devicedetection_examples"
./python/run-integration-tests.ps1 -RepoName $RepoName -Packages $packages -Keys $Keys

exit $LASTEXITCODE
