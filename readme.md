![51Degrees](https://51degrees.com/DesktopModules/FiftyOne/Distributor/Logo.ashx?utm_source=github&utm_medium=repository&utm_content=readme_main&utm_campaign=python-open-source "THE Fastest and Most Accurate Device Detection") **v4 Device Detection Python**

[Pipeline Documentation](https://docs.51degrees.com?utm_source=github&utm_medium=repository&utm_content=documentation&utm_campaign=python-open-source "advanced developer documentation") | [Available Properties](https://51degrees.com/resources/property-dictionary?utm_source=github&utm_medium=repository&utm_content=property_dictionary&utm_campaign=python-open-source "View all available properties and values")

## Introduction
This project contains 51Degrees Device Detection engines that can be used with the [Pipeline API]

The Pipeline is a generic web request intelligence and data processing solution with the ability to add a range of 51Degrees and/or custom plug ins (Engines) 

## Device detection

Device detection can be performed using the 51Degrees cloud service. 

## Requirements and installation

* Python 2.7 or Python 3
* The `flask` python library to run the web examples

## Running examples

To run examples from this folder:

`python3 -m examples.cloud.gettingstarted`

To run the web example:

### Linux

Execute `export FLASK_APP=` with the name of the web example file, then `flask run`.

### Windows

Execute `$env:FLASK_APP = "x"` with the name of the example file, then `flask run`.
