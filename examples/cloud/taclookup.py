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

@example cloud/taclookup.py

@include{doc} example-tac-lookup-cloud.txt

Example output:

```
This example shows the details of devices associated with a given 'Type Allocation Code' or 'TAC'.
More background information on TACs can be found through various online sources such as Wikipedia: https://en.wikipedia.org/wiki/Type_Allocation_Code
----------------------------------------
Which devices are associated with the tac: 35925406
Apple ['iPhone 6'] A1586

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

    # we get a tac to test
    tac = "35925406"

    # We create a FlowData object from the pipeline
    # this is used to add evidence to and then process
    flowData = pipeline.createFlowData()

    # After creating a flowdata instance, add the native model name as evidence.
    flowData.evidence.set('query.tac', tac)

    # Now we process the FlowData to get results

    flowData.process()

    # The result is an array containing the details of any devices that match
    # the specified tac.
    # The code in this example iterates through this array, outputting the
    # vendor and model of each matching device.
    
    print("Which devices are associated with the tac: " + tac) 

    for profile in flowData.hardware.profiles:
        hardwareVendor = profile["hardwarevendor"]
        hardwareName = profile["hardwarename"]
        hardwareModel = profile["hardwaremodel"]

        if (hardwareVendor.hasValue and hardwareName.hasValue and hardwareModel.hasValue):
            print(hardwareVendor.value() + " " + str(hardwareName.value()) +" "+ hardwareModel.value())
        else:
            print(hardwareVendor.noValueMessage)
