param (
    [Parameter(Mandatory=$true)]
    [string]$RepoName
)

$perfResults = New-Item -ItemType directory -Path $RepoName/test-results/performance-summary -Force

Push-Location $RepoName
try {
	Write-Output "Running performance tests"
	$results = python fiftyone_devicedetection_examples/performance-tests/benchmark.py ../assets/51Degrees-LiteV4.1.hash ../assets/"20000 User Agents.csv" || $(throw "benchmark failed with code: $LASTEXITCODE")
	Write-Output "Writing results"
	$results | Out-File $perfResults/results_$RepoName.json
} finally {
	Pop-Location
}
