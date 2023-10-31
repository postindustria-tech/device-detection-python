Set-Location -Path "..\fiftyone_devicedetection_onpremise\"

# Check if _DeviceDetectionHashEngineModule.pyd exists and delete it if it does
if (Test-Path -Path ".\fiftyone_devicedetection_onpremise\_DeviceDetectionHashEngineModule.pyd") {
    Remove-Item ".\fiftyone_devicedetection_onpremise\_DeviceDetectionHashEngineModule.pyd"
}

# Build the module
python setup.py build_clib build_ext --inplace
