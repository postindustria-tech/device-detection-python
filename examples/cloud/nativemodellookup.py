# *********************************************************************
# This Original Work is copyright of 51 Degrees Mobile Experts Limited.
# Copyright 2019 51 Degrees Mobile Experts Limited, 5 Charlotte Close,
# Caversham, Reading, Berkshire, United Kingdom RG4 7BY.
#
# This Original Work is licensed under the European Union Public Licence (EUPL) 
# v.1.2 and is subject to its terms as set out below.
#
# If a copy of the EUPL was not distributed with this file, You can obtain
# one at https://opensource.org/licenses/EUPL-1.2.
#
# The 'Compatible Licences' set out in the Appendix to the EUPL (as may be
# amended by the European Commission) shall be deemed incompatible for
# the purposes of the Work and the provisions of the compatibility
# clause in Article 5 of the EUPL shall not apply.
# 
# If using the Work as, or as part of, a network application, by 
# including the attribution notice(s) required under Article 5 of the EUPL
# in the end user terms of the application under an appropriate heading, 
# such notice(s) shall fulfill the requirements of that article.
# ********************************************************************

"""

@example cloud/nativeModelLookup.py

@include{doc} example-native-model-lookup-cloud.txt

Example output:

```
This example finds the details of devices from the 'native model name'.
The native model name can be retrieved by code running on the device (For example, a mobile app).
For Android devices, see https://developer.android.com/reference/android/os/Build#MODEL
For iOS devices, see https://gist.github.com/soapyigu/c99e1f45553070726f14c1bb0a54053b#file-machinename-swift
----------------------------------------
Which devices are associated with the native model name 'SC-03L'?
        Samsung Galaxy S10 (SC-03L)
```

"""

from fiftyone_pipeline_core.pipelinebuilder import PipelineBuilder
from fiftyone_pipeline_cloudrequestengine.cloudrequestengine import CloudRequestEngine
from fiftyone_pipeline_devicedetection.hardwareprofile_cloud import HardwareProfileCloud

# You need to create a resource key at https://configure.51degrees.com
# and paste it into the code, replacing !!YOUR_RESOURCE_KEY!! below.

resourceKey = "!!YOUR_RESOURCE_KEY!!"

if resourceKey == "!!YOUR_RESOURCE_KEY!!":
    print("""
    You need to create a resource key at
    https://configure.51degrees.com and paste it into the code,
    'replacing !!YOUR_RESOURCE_KEY!!
    make sure to include the HardwareName, HardwareProfile and HardwareVendor
    properties used by this example
    """)
else:

    # Create an instance of the cloud request engine with your resource key
    
    requestEngineInstance = CloudRequestEngine({
        "resourceKey": resourceKey
    })

    # Now create an instance of the hardwareprofile cloud engine

    hardwareProfileEngineInstance = HardwareProfileCloud()

    # Now create a pipeline and add those two engines
    # the Cloud Request Engine needs to go first

    pipeline = PipelineBuilder().add(requestEngineInstance).add(hardwareProfileEngineInstance).build()

    # we get a native model name to test
    nativeModelAndroid = 'SC-03L'

    # We create a FlowData object from the pipeline
    # this is used to add evidence to and then process
    flowData = pipeline.createFlowData()

    # After creating a flowdata instance, add the native model name as evidence.
    flowData.evidence.set('query.nativemodel', nativeModelAndroid)

    # Now we process the FlowData to get results

    flowData.process()

    # The result is an array containing the details of any devices that match
    # the specified native model name.
    # The code in this example iterates through this array, outputting the
    # vendor and model of each matching device.
    
    print("Which devices are associated with the native model name: " + nativeModelAndroid) 

    for profile in flowData.hardware.profiles:
        hardwareVendor = profile["hardwarevendor"]
        hardwareName = profile["hardwarename"]
        hardwareModel = profile["hardwaremodel"]

        if (hardwareVendor.hasValue and hardwareName.hasValue and hardwareModel.hasValue):
            print(hardwareVendor.value() + " " + str(hardwareName.value()) +" "+ hardwareModel.value())
        else:
            print(hardwareVendor.noValueMessage)

