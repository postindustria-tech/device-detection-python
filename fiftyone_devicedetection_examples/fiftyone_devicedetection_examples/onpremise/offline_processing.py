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

## @example onpremise/offline_processing.py
# 
# @include{doc} example-offline-processing-hash.txt
# 

import csv
import time
import multiprocessing as mp
from fiftyone_devicedetection_examples.example_utils import ExampleUtils
# This example goes through a CSV of 20000 user agents and processes them, 
# saving whether each one is a mobile, not, or unknown to a csv file

from fiftyone_devicedetection_onpremise.devicedetection_onpremise_pipelinebuilder import DeviceDetectionOnPremisePipelineBuilder

# First we create the device detection pipeline with the desired settings.

data_file = ExampleUtils.find_file("51Degrees-LiteV4.1.hash")

pipeline = DeviceDetectionOnPremisePipelineBuilder(
    data_file_path=data_file,
    licence_keys="",
    performance_profile='MaxPerformance',
    add_javascript_builder = False, 
    restricted_properties = ["ismobile"],
    usage_sharing=False, 
    auto_update=False).build()

# Here we make a function that processes a user agent
# And returns if it is a mobile device

def process_user_agent(user_agent):

    # First we create the flowdata using the global pipeline
    flowdata = pipeline.create_flowdata()

    # Here we add the user agent as evidence
    flowdata.evidence.add("header.user-agent", user_agent)

    # We process the flowdata to get the results
    flowdata.process()

    # To check whether the User-Agent is a mobile device we look at the 
    # ismobile property inside the Device Detection Engine

    # first we check if this has a meaningful result

    if flowdata.device.ismobile.has_value():
        return flowdata.device.ismobile.value()
    else:
        return None

# First we read the contents of the 2000 user agents file
# Converting it to a list

with open(ExampleUtils.find_file('20000 User Agents.csv'), newline='') as file:
    reader = csv.reader(file)
    user_agents = list(reader)

number_of_user_agents = len(user_agents)

print("Processing " + str(number_of_user_agents) + " user agents")

# Now we write to a csv file the user agent and the result if ismobile

output_path = "output.csv"
count = 0

with open(output_path,'w') as file:
    for user_agent in user_agents:
        result = process_user_agent(user_agent[0])
        file.write(user_agent[0])
        file.write(",")
        file.write(str(result))
        file.write('\n')
        count += 1

print("Processed " + str(count) + " user agents")