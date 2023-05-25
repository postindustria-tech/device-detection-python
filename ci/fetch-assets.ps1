param (
    [Parameter(Mandatory=$true)]
    [string]$RepoName,
    [Parameter(Mandatory=$true)]
    [string]$DeviceDetection,
    [string]$DeviceDetectionUrl
)

$ErrorActionPreference = 'Stop'

./steps/fetch-hash-assets.ps1 -RepoName $RepoName -LicenseKey $DeviceDetection -Url $DeviceDetectionUrl
Move-Item -Path $RepoName/TAC-HashV41.hash -Destination $RepoPath/fiftyone_devicedetection_onpremise/fiftyone_devicedetection_onpremise/device-detection-cxx/

Write-Output "Downloading Lite file"
Invoke-WebRequest -Uri 'https://github.com/51Degrees/device-detection-data/raw/main/51Degrees-LiteV4.1.hash' `
    -OutFile "$RepoPath/fiftyone_devicedetection_onpremise/fiftyone_devicedetection_onpremise/device-detection-cxx/51Degrees-LiteV4.1.hash"

Write-Output "Downloading Evidence file"
Invoke-WebRequest -Uri 'https://media.githubusercontent.com/media/51Degrees/device-detection-data/main/20000%20Evidence%20Records.yml' `
    -OutFile "$RepoPath/fiftyone_devicedetection_onpremise/fiftyone_devicedetection_onpremise/device-detection-cxx/20000 Evidence Records.yml"

Write-Output "Downloading Agents file"
Invoke-WebRequest -Uri 'https://media.githubusercontent.com/media/51Degrees/device-detection-data/main/20000%20User%20Agents.csv' `
    -OutFile "$RepoPath/fiftyone_devicedetection_onpremise/fiftyone_devicedetection_onpremise/device-detection-cxx/20000 User Agents.csv"
