# 51Degrees Device Detection Engines

![51Degrees](https://51degrees.com/DesktopModules/FiftyOne/Distributor/Logo.ashx?utm_source=github&utm_medium=repository&utm_content=readme_main&utm_campaign=python-open-source "THE Fastest and Most Accurate Device Detection") **v4 Device Detection Python**

[Developer Documentation](https://51degrees.com/device-detection-python/index.html?utm_source=github&utm_medium=repository&utm_content=property_dictionary&utm_campaign=python-open-source "Developer Documentation") | [Available Properties](https://51degrees.com/resources/property-dictionary?utm_source=github&utm_medium=repository&utm_content=property_dictionary&utm_campaign=python-open-source "View all available properties and values")

## Introduction

This project contains 51Degrees Device Detection engines that can be used with the Pipeline API.

The Pipeline is a generic web request intelligence and data processing solution with the ability to add a range of 51Degrees and/or custom plug ins (Engines)

This git repository uses submodules, to clone the git repository run:

```bash
git clone --recurse-submodules https://github.com/51Degrees/device-detection-python.git
```

or if already cloned run the following to obtain all sub modules.:

```bash
git submodule update --init --recursive
```

## Requirements

* Python 3.5+
* The `flask` python library to run the web examples
* Git Large File System (LFS) for sub module device-detection-cxx\device-detection-data
* Additional requirements are for the on-premise Device-Detection Engine.
* On Windows
  * Visual Studio 2019 or equivalent [C++ build tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
    * Minimum Platform Toolset Version `v142`
    * Minimum Windows SDK Version `10.0.18362.0`
## Folders

* `fiftyone_devicedetection` - references both cloud and on-premise packages, contains generic Device-Detection Pipeline Builder.
  * `examples` - examples for switching between cloud and on-premise.
* `fiftyone_devicedetection_cloud` - cloud implementation of the engines.
  * `tests` - tests for the cloud engine and examples.
* `fiftyone_devicedetection_onpremise` - uses a native library which is built during setup to provide optimal performance and low latency device detections.
  * `tests` - tests for the on-premise engine.
* `fiftyone_devicedetection_shared` - common components used by the cloud and on-premise packages.
* `fiftyone_devicedetection_examples` - cloud and on-premise examples.
  * `tests` - tests for the examples.

## Installation

### PyPi

To install all packages, run:

```bash
python -m pip install fiftyone-devicedetection
```

The `fiftyone-devicedetection` package references both cloud and on-premise packages. If you do 
not want the on-premise engine or cannot meet the requirements for installing on-premise then 
install the cloud package on its own:

```bash
python -m pip install fiftyone-devicedetection-cloud
```

See the cloud package readme for more details specifics.

### GitHub

It is recommended to use Pipenv when build packages. Pipenv will ensure all the required packages 
for building and testing are available e.g. `cython` and `flask`.

```bash
python -m pip install pipenv
pipenv install
pipenv shell
```

There are various methods to build and install the packages.

```bash
make install
```

other make targets:

* `cloud` - only setup packages required for cloud
* `onpremise` - only setup packages required for onpremise
* `test` - run package tests
* `clean` - remove temporary files created when building extensions

For convenience, there is also a powershell setup script called `setup.ps1`. To run it, you may 
need to update the execution policy to allow unsigned scripts to execute:

```powershell
Set-ExecutionPolicy -Scope CurrentUser Bypass

.\setup.ps1
```

If you want to perform the steps manually, these are the commands to build the native on-premise
library and install the packages.

```bash
python -m pip install -e fiftyone_devicedetection_shared/
python -m pip install -e fiftyone_devicedetection_cloud/
cd fiftyone_devicedetection_onpremise/
python setup.py build_clib build_ext
cd ../
python -m pip install -e fiftyone_devicedetection_onpremise/
python -m pip install -e fiftyone_devicedetection/
```

## Examples

Then, to run an example, navigate into the example module directory.

```bash
cd fiftyone_devicedetection_examples/
```

Then run an example:

```bash
python -m fiftyone_devicedetection_examples.cloud.gettingstarted_console
```

#### Cloud

| Example                                | Revamped           | Description |
|----------------------------------------|--------------------|-------------|
| gettingstarted_console                 | @tick              | How to use the 51Degrees Cloud service to determine details about a device based on its User-Agent and User-Agent Client Hints HTTP header values. |
| gettingstarted_web                     | @tick              | How to use the 51Degrees Cloud service to determine details about a device as part of a simple ASP.NET website. |
| taclookup                              |                    | How to get device details from a TAC (Type Allocation Code) using the 51Degrees cloud service. |
| nativemodellookup                      |                    | How to get device details from a native model name using the 51Degrees cloud service. |
| failuretomatch                         |                    | Demonstrate the features that are available when a match cannot be found. |
| metadata                               |                    | How to access the meta-data for the device detection data model. For example, information about the  available properties. |
| useragentclienthints-web               |                    | Legacy example. Retained for the associated automated tests. See GettingStarted-Web instead. |

#### On-Premise

| Example                                | Revamped           | Description |
|----------------------------------------|--------------------|-------------|
| gettingstarted_console                 | @tick              | How to use the 51Degrees on-premise device detection API to determine details about a device based on its User-Agent and User-Agent Client Hints HTTP header values. |
| gettingstarted_web                     | @tick              | How to use the 51Degrees Cloud service to determine details about a device as part of a simple ASP.NET website. |
| failuretomatch                         |                    | Demonstrate the features that are available when a match cannot be found. |
| match_metrics                          |                    | How to access the metrics that relate to the device detection algorithm. |
| metadata                               |                    | How to access the meta-data for the device detection data model. For example, information about the  available properties. |
| offline_processing                     |                    | Example showing how to ingest a file containing data from web requests and perform detection against the entries. |
| performance                            |                    | How to configure the various performance options and run a simple performance test. |
| useragentclienthints-web               |                    | Legacy example. Retained for the associated automated tests. See GettingStarted-Web instead. |

