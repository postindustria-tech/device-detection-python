param (
    [Parameter(Mandatory=$true)]
    [string]$RepoName,
    [Parameter(Mandatory=$true)]
    [string]$DeviceDetection,
    [string]$DeviceDetectionUrl
)

if ($env:GITHUB_JOB -eq "PreBuild") {
    Write-Output "Skipping assets fetching"
    exit 0
}

$ErrorActionPreference = 'Stop'

$assets = New-Item -ItemType Directory -Path assets -Force
$deviceDetectionData = "$RepoName/fiftyone_devicedetection_onpremise/fiftyone_devicedetection_onpremise/device-detection-cxx/device-detection-data"

$urls = @{
    "51Degrees-LiteV4.1.hash" = "https://github.com/51Degrees/device-detection-data/raw/main/51Degrees-LiteV4.1.hash"
    "20000 Evidence Records.yml" = "https://media.githubusercontent.com/media/51Degrees/device-detection-data/main/20000%20Evidence%20Records.yml"
    "20000 User Agents.csv" = "https://media.githubusercontent.com/media/51Degrees/device-detection-data/main/20000%20User%20Agents.csv"
    "51Degrees-Tac.zip" = "https://storage.googleapis.com/51degrees-assets/$DeviceDetection/51Degrees-Tac.zip"
}

if (!(Test-Path "$assets/TAC-HashV41.hash")) {
    ./steps/fetch-hash-assets.ps1 -RepoName $RepoName -LicenseKey $DeviceDetection -Url $DeviceDetectionUrl
    Move-Item -Path $RepoName/TAC-HashV41.hash -Destination $assets
} else {
    Write-Output "'$assets/TAC-HashV41.hash' exists, skipping download"
}

foreach ($file in $urls.Keys) {
    if (!(Test-Path $file)) {
        Invoke-WebRequest -Uri $urls[$file] -OutFile "$assets/$file"
    } else {
        Write-Output "'$file' exists, skipping download"
    }
}

# Tests mutate this file, so we copy it
Write-Output "Copying 'TAC-HashV41.hash' to '$deviceDetectionData/Enterprise-HashV41.hash'"
Copy-Item -Path $assets/TAC-HashV41.hash -Destination $deviceDetectionData/Enterprise-HashV41.hash

# We can just symlink these
New-Item -ItemType SymbolicLink -Force -Target "$assets/51Degrees-LiteV4.1.hash" -Path "$deviceDetectionData/51Degrees-LiteV4.1.hash"
New-Item -ItemType SymbolicLink -Force -Target "$assets/20000 Evidence Records.yml" -Path "$deviceDetectionData/20000 Evidence Records.yml"
New-Item -ItemType SymbolicLink -Force -Target "$assets/20000 User Agents.csv" -Path "$deviceDetectionData/20000 User Agents.csv"

# This one needs extraction (10GB file inside, can't cache it uncompressed)
Write-Output "Extracting '51Degrees-Tac.zip'"
Expand-Archive -Path $assets/51Degrees-Tac.zip -DestinationPath $RepoName/fiftyone_devicedetection_cloud/tests/
Rename-Item -Path $RepoName/fiftyone_devicedetection_cloud/tests/51Degrees-Tac-All.csv -NewName 51Degrees.csv
