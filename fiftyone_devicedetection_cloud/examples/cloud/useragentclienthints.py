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

## @example cloud/useragentclienthints.py
# 
# @include{doc} example-user-agent-client-hints.txt
# 
# @include{doc} example-require-resourcekey.txt
#
# Expected output:
# 
# ```
# ---------------------------------------
# This example demonstrates detection using user-agent client hints.
# The sec-ch-ua value can be used to determine the browser of the connecting device, but not other components such as the hardware.
# We show this by first performing detection with sec-ch-ua only.
# We then repeat with the user-agent header set as well. Note that the client hint takes priority over the user-agent.
# Finally, we use both sec-ch-ua and user-agent.Note that sec-ch-ua takes priority over the user-agent for detection of the browser.
# ---------------------------------------
# Sec-CH-UA = '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"'
# User-Agent = 'NOT_SET'
#         Browser = Chrome 89
#         IsMobile = No matching profiles could be found for the supplied evidence.A 'best guess' can be returned by configuring more lenient matching rules.See https://51degrees.com/documentation/_device_detection__features__false_positive_control.html
#
# Sec-CH-UA = 'NOT_SET'
# User-Agent = 'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
#         Browser = Samsung Browser 10.1
#         IsMobile = True
#
# Sec-CH-UA = '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"'
# User-Agent = 'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
#         Browser = Chrome 89
#         IsMobile = True
# ```
#

from fiftyone_devicedetection_cloud.devicedetection_cloud_pipelinebuilder import DeviceDetectionCloudPipelineBuilder

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
    To include the properties used in this example, go to https://configure.51degrees.com/
    """)
else:

    # First create the device detection pipeline with the desired settings.

    print("---------------------------------------");
    print("This example demonstrates detection " +
                    "using user-agent client hints.\n")
    print("The sec-ch-ua value can be used to " +
                    "determine the browser of the connecting device, " +
                    "but not other components such as the hardware.\n")
    print("We show this by first performing " +
                    "detection with sec-ch-ua only.\n")
    print("We then repeat with the user-agent " +
                    "header set as well. Note that the client hint takes " +
                    "priority over the user-agent.\n")
    print("Finally, we use both sec-ch-ua and " +
                "user-agent. Note that sec-ch-ua takes priority " +
                "over the user-agent for detection of the browser.\n")
    print("---------------------------------------\n")

    mobile_ua = "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) " + \
                        "AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 " + \
                            "Chrome/71.0.3578.99 Mobile Safari/537.36"
    secchua_value = '\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"'

    pipeline = DeviceDetectionCloudPipelineBuilder({
        "resource_key": resource_key
    }).build()

    # Define function to analyze user-agent/client hints

    def analyze_client_hints(pipeline, setUserAgent, setSecChUa):
        
        # We create a FlowData object from the pipeline
        # this is used to add evidence to and then process  
        flowdata = pipeline.create_flowdata()

        # Add a value for the user-agent client hints header
        # sec-ch-ua as evidence 
        if setSecChUa:
            flowdata.evidence.add("query.sec-ch-ua", secchua_value)

        # Also add a   user-agent if requested 
        if setUserAgent:
            flowdata.evidence.add("query.user-agent", mobile_ua)

        flowdata.process()

        device = flowdata.device

        browser_name = device.browsername
        browser_version = device.browserversion
        ismobile = device.ismobile

        # Output evidence
        secchua = "NOT_SET"
        if setSecChUa:
            secchua = secchua_value
        print("Sec-CH-UA = '{}'\n".format(secchua))

        ua = "NOT_SET"
        if setUserAgent:
            ua = mobile_ua  
        print("User-Agent = '{}'\n".format(ua))

        # Output the Browser
        if (browser_name.has_value() and browser_version.has_value()):
            print("\tBrowser = {} {}\n".format(browser_name.value(), browser_version.value()))
        elif (browser_name.has_value()):
            print("\tBrowser = {} (version unknown)\n".format(browser_name.value()))
        else:
            print("\tBrowser = {}\n".format(browser_name.no_value_message()))

        # Output the value of the 'IsMobile' property.
        if (ismobile.has_value()): 
            print("\tIsMobile = {}\n\n".format(ismobile.value()))
        else:
            print("\tIsMobile = {}\n\n".format(ismobile.no_value_message()))

    # first try with just sec-ch-ua.
    analyze_client_hints(pipeline, False, True)

    # Now with just user-agent.
    analyze_client_hints(pipeline, True, False)

    # Finally, perform detection with both.
    analyze_client_hints(pipeline, True, True)

