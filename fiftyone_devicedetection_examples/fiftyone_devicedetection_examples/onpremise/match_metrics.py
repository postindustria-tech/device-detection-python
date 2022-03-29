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

## @example onpremise/match_metrics.py
# 
# @include{doc} example-match-metrics-hash.txt
# 
#

from fiftyone_devicedetection_onpremise.devicedetection_onpremise_pipelinebuilder import DeviceDetectionOnPremisePipelineBuilder
from fiftyone_devicedetection_examples.example_utils import ExampleUtils

# First create the device detection pipeline with the desired settings.

data_file = ExampleUtils.find_file("51Degrees-LiteV4.1.hash")

pipeline = DeviceDetectionOnPremisePipelineBuilder(
    data_file_path = data_file, 
    licence_keys = "", 
    performance_profile = 'MaxPerformance', 
    auto_update=False).build()

# Now we can take a User-Agent and run it through this pipeline

# First we create a FlowData object from the pipeline
flowdata = pipeline.create_flowdata()

# Then we add the User-Agent we are interested in as evidence
iphone_ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114"

flowdata.evidence.add("header.user-agent", iphone_ua)

# Now we process the FlowData using the engines in the Pipeline

flowdata.process()

# The device detection engine comes with additional metadata about each match

if flowdata.device.deviceid.has_value():
    print('Device ID: ' + str(flowdata.device.deviceID.value()))
    print("""
    Consists of four components separated by a hyphen symbol:
    Hardware-Platform-Browser-IsCrawler where each Component
    represents an ID of the corresponding Profile.""")

if  flowdata.device.useragents.has_value():
    print('Matched useragents: ' + str(flowdata.device.useragents.value()))
    print("The matched useragents")

if flowdata.device.difference.has_value():
    print('Difference: ' + str(flowdata.device.difference.value()))
    print("""
    Used when detection method is not Exact or None.
    This is an integer value and the larger the value
    the less confident the detector is in this result.""")

if flowdata.device.method.has_value():
    print('Method: ' + str(flowdata.device.method.value()))
    print("""Provides information about the algorithm that was used to perform detection for a particular User-Agent.""")

if  flowdata.device.matchednodes.has_value():
    print('Method: ' + str(flowdata.device.matchednodes.value()))
    print("""
    The number of hash nodes that have been matched before finding a result.""")