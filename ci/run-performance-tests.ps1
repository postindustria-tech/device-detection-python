param (
    [Parameter(Mandatory=$true)]
    [string]$RepoName,
    [Parameter(Mandatory=$true)]
    [string]$Name,
    [boolean]$RunPerformance = $True
)

if (!$RunPerformance) {
    Write-Output "Skipping performance tests"
    exit 0
}

$perfSummary = New-Item -ItemType directory -Path $RepoName/test-results/performance-summary -Force

Push-Location $RepoName
try {
    Write-Output "Running performance tests"
    python fiftyone_devicedetection_examples/performance-tests/test_performance.py ../assets/51Degrees-LiteV4.1.hash ../assets/"20000 User Agents.csv" || $(throw "benchmark failed with code: $LASTEXITCODE")
    Get-Content -Path performance_test_summary.json
    Move-Item -Path performance_test_summary.json -Destination $perfSummary/results_$Name.json || $(throw "failed to move summary")
    Write-Output "OK"
} finally {
    Pop-Location
}
