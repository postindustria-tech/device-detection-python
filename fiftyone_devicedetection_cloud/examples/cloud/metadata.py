# *********************************************************************
# This Original Work is copyright of 51 Degrees Mobile Experts Limited.
# Copyright 2022 51 Degrees Mobile Experts Limited, Davidson House,
# Forbury Square, Reading, Berkshire, United Kingdom RG1 3EU.
#
# This Original Work is licensed under the European Union Public Licence
# (EUPL) v.1.2 and is subject to its terms as set out below.
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
# ********************************************************************* 

## @example cloud/metadata.py
# 
# @include{doc} example-metadata-cloud.txt
# 
# @include{doc} example-require-resourcekey.txt
# 
# Expected output:
# 
# ```
# [List of properties with names and categories]
# 
# Does user agent Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 support svg? :
# true
# Does user agent Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 support video? :
# true
# Does user agent Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 support supportstls/ssl? :
# true
# Does user agent Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 support supportswebgl? :
# true
# ```


from fiftyone_devicedetection_cloud.devicedetection_cloud_pipelinebuilder import DeviceDetectionCloudPipelineBuilder

# First create the device detection pipeline with the desired settings.

# You need to create a resource key at https://configure.51degrees.com
# and paste it into the code, replacing !!YOUR_RESOURCE_KEY!! below.
# Alternatively, add a resource_key environment variable
import os
if "resource_key" in os.environ:
    resource_key = os.environ["resource_key"]
else:
    resource_key = "!!YOUR_RESOURCE_KEY!!"

if resource_key == "!!YOUR_RESOURCE_KEY!!":
    print("""
    You need to create a resource key at
    https://configure.51degrees.com and paste it into the code,
    'replacing !!YOUR_RESOURCE_KEY!!
    To include the properties used by this example go to https://configure.51degrees.com/CfLML6rg
    """)
else:

    pipeline = DeviceDetectionCloudPipelineBuilder({
        "resource_key": resource_key
    }).build()

    # Now we see what properties are available in the pipeline

    properties = pipeline.get_properties()

    # Now we find out the details of the properties in the device engine

    for property_key, property_meta in properties["device"].items():
         print(property_key + " of category " + property_meta["category"])

    # Now we can take a User-Agent, run it through this pipeline and check 
    # the supported media properties against it

    # First we create a FlowData object from the pipeline
    flowdata = pipeline.create_flowdata()

    # Then we add the User-Agent we are interested in as evidence
    iphone_ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114"

    flowdata.evidence.add("header.user-agent", iphone_ua)

    # Now we process the FlowData using the engines in the Pipeline

    flowdata.process()

    # To get all properties of a specific category, we can use the "getWhere" function

    mediaSupport = flowdata.get_where("category", "Supported Media")

    for supportedMediaProperty, supportedValue in mediaSupport.items():
        print("Does User-Agent " + iphone_ua + " support " + supportedMediaProperty + "?")
        if supportedValue.has_value():
            print(supportedValue.value())
        else:
            print(supportedValue.no_value_message())
