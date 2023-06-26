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
    $resultsRaw = python fiftyone_devicedetection_examples/performance-tests/test_performance.py ../assets/51Degrees-LiteV4.1.hash ../assets/"20000 User Agents.csv" --output || $(throw "benchmark failed with code: $LASTEXITCODE")
    Write-Output $resultsRaw

    $results = $resultsRaw | ConvertFrom-Json
    @{
        HigherIsBetter = @{
            DetectionsPerSecond = $results.DetectionsPerSecond
        };
        LowerIsBetter = @{
            AvgMillisecsPerDetection = $results.AvgMillisecsPerDetection
        }
    } | ConvertTo-Json | Out-File $perfSummary/results_$Name.json
} finally {
    Pop-Location
}
