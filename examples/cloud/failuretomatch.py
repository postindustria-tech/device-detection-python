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
@example cloud/failuretomatch.py

@include{doc} example-failure-to-match-cloud.txt

@include{doc} example-require-resourcekey.txt

Expected output:

```
Is user agent '--' a mobile?
The results contained a null profile for the component which the required property belongs to.

Is user agent 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114' a mobile?
true
```

"""

from fiftyone_pipeline_devicedetection.devicedetection_pipelinebuilder import DeviceDetectionPipelineBuilder

# First create the device detection pipeline with the desired settings.

# You need to create a resource key at https://configure.51degrees.com
# and paste it into the code, replacing !!YOUR_RESOURCE_KEY!! below.

resourceKey = "!!YOUR_RESOURCE_KEY!!"

if resourceKey == "!!YOUR_RESOURCE_KEY!!":
    print("""
    You need to create a resource key at
    https://configure.51degrees.com and paste it into the code,
    'replacing !!YOUR_RESOURCE_KEY!!
    To include the properties used in this example, go to https://configure.51degrees.com/bxXqZhLT
    """)
else:

    pipeline = DeviceDetectionPipelineBuilder({"resourceKey": resourceKey}).build()

    # We create a FlowData object from the pipeline
    # this is used to add evidence to and then process

    flowData1 = pipeline.createFlowData()

    # Here we add a User-Agent of an iphone as evidence

    iphoneUA = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114"
    
    flowData1.evidence.set("header.user-agent", iphoneUA)

    # Now we process the FlowData

    flowData1.process()

    # To check whether the User-Agent is a mobile device we look at the ismobile property
    # inside the Device Detection Engine

    # first we check if this has a meaningful result

    print("Is User-Agent " + iphoneUA + " a mobile device?: ") 
    if flowData1.device.ismobile.hasValue():
        print(flowData1.device.ismobile.value())
    else:
        # Output why the value isn't meaningful
        print(flowData1.device.ismobile.noValueMessage)

    # Now we do the same with a new User-Agent, this time a corrupted one

    badUA = "--"
    
    flowData2 = pipeline.createFlowData()

    flowData2.evidence.set("header.user-agent", badUA)

    flowData2.process()

    print("Is User-Agent " + badUA + " a mobile device?: ") 
    if flowData2.device.ismobile.hasValue():
        print(flowData2.device.ismobile.value())
    else:
        # Output why the value isn't meaningful
        print(flowData2.device.ismobile.noValueMessage)
