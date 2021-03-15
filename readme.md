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
* Additional requirements are required for the on-premise Device-Detection Engine.

## Folders

* `fiftyone_devicedetection` - references both cloud and on-premise packages, contains generic Device-Detection Pipeline Builder.
  * `examples` - examples for switching between cloud and on-premise.
* `fiftyone_devicedetection_cloud` - cloud implementation of the engines.
  * `examples` - examples for cloud device-detection.
  * `tests` - tests for the cloud engine and examples.
* `fiftyone_devicedetection_onpremise` - uses a native library which is built during setup to provide optimal performance and low latency device detections.
  * `examples` - examples for on-premise device-detection.
  * `tests` - tests for the on premise engine and examples.
* `fiftyone_devicedetection_shared` - common components used by the cloud and on-premise packages.

## Installation

### PyPi

To install all packages, run:

```bash
python -m pip install fiftyone-devicedetection
```

The `fiftyone-devicedetection` package references both cloud and on-premise packages. If you do not want the on-premise engine or cannot meet the requirements for installing on-premise then install the cloud package on its own:

```bash
python -m pip install fiftyone-devicedetection-cloud
```

See the cloud package readme for more details specifics.

### GitHub

It is recommended to use Pipenv when build packages. Pipenv will ensure all the required packages for building and testing are available e.g. `cython` and `flask`.

```bash
python -m pip install pipenv
pipenv install
pipenv shell
```

To install packages for development run the following commands:

```bash
python -m pip install -e fiftyone_devicedetection_shared/
python -m pip install -e fiftyone_devicedetection_cloud/
cd fiftyone_devicedetection_onpremise/
python setup.py build_clib build_ext
cd ../
python -m pip install -e fiftyone_devicedetection_onpremise/
python -m pip install -e fiftyone_devicedetection/
```

Alternatively, if you have make installed you can run the make file:

```bash
make
```

```bash
make install
```

other targets:

* `cloud` - only setup packages required for cloud
* `onpremise` - only setup packages required for onpremise
* `test` - run package tests
* `clean` - remove temporary files created when building extensions

For convenience, there is also a powershell setup script called `setup.ps1`. To run it, you may need to update the execution policy to allow unsigned scripts to execute:

```powershell
Set-ExecutionPolicy -Scope CurrentUser Bypass

.\setup.ps1
```

## Examples

Then, to run an example, navigate into one of the module directories that contain an examples subfolder, e.g.

```bash
cd fiftyone_devicedetection/
```

Then run an example:

```bash
python -m examples.gettingstarted
```
