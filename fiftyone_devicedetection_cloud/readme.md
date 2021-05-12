# 51Degrees Device Detection Engines - Cloud

![51Degrees](https://51degrees.com/DesktopModules/FiftyOne/Distributor/Logo.ashx?utm_source=github&utm_medium=repository&utm_content=readme_main&utm_campaign=python-open-source "THE Fastest and Most Accurate Device Detection") **v4 Device Detection Python**

[Developer Documentation](https://51degrees.com/device-detection-python/index.html?utm_source=github&utm_medium=repository&utm_content=property_dictionary&utm_campaign=python-open-source "Developer Documentation") | [Available Properties](https://51degrees.com/resources/property-dictionary?utm_source=github&utm_medium=repository&utm_content=property_dictionary&utm_campaign=python-open-source "View all available properties and values")

## Introduction

### From PyPi

`pip install fiftyone-devicedetection-cloud`

You can confirm this is working with the following micro-example.

* Create a resource key for free with the 51Degrees [configurator](https://configure.51degrees.com/np5M4nlF). This defines the properties you want to access.
* On the 'implement' page of the configurator, copy the resource key and replace YOUR_RESOURCE_KEY in the example below. Save this as exampledd.py
* Run the example with `python exampledd.py`
* Feel free to try different user-agents and property values.

```python
from fiftyone_devicedetection_cloud.devicedetection_cloud_pipelinebuilder import DeviceDetectionCloudPipelineBuilder
pipeline = DeviceDetectionCloudPipelineBuilder({"resource_key": "YOUR_RESOURCE_KEY"}).build()
fd = pipeline.create_flowdata()
fd.evidence.add("header.user-agent", "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")
fd.process()
print(fd.device.ismobile.value())
```

For more in-depth examples, check out the [examples](https://51degrees.com/device-detection-python/examples.html) page in the documentation.

### From GitHub

If you've cloned the GitHub repository, you will be able to run the examples directly:

`python -m examples.cloud.gettingstarted`

To run the web example navigate into examples/cloud folder:

#### Linux

Execute `export FLASK_APP=web` where `web` is the example file, and start your application via `flask run`.

#### Windows

Execute `$env:FLASK_APP = "web"` where `web` is the example file, and start your application via `flask run`.

## Tests

To run the tests use:

`python -m unittest discover -s tests -p test*.py -b`

Cloud tests will only run with a valid 51Degrees resource key (see above) set as a resource_key operating system environment variable.

For example, use following command to set resource_key on Linux:
`export resource_key=MY-RESOURCE-KEY`

On Microsoft Windows use:
`$env:resource_key = "MY-RESOURCE-KEY"`

As the performance and offline processing tests take longer than the others, there is another environment variable flag to run those:

Linux:
`export run_performance_tests=true`

Microsoft Windows:
`$env:run_performance_tests = "true"`
