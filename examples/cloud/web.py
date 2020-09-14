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
@example cloud/web.py

@include{doc} example-web-integration.txt

@include{doc} example-require-resourcekey.txt

"""

from fiftyone_pipeline_devicedetection.devicedetection_pipelinebuilder import DeviceDetectionPipelineBuilder
from fiftyone_pipeline_core.web import webevidence
import json

# First create the device detection pipeline with the desired settings.

# You need to create a resource key at https://configure.51degrees.com
# and paste it into the code, replacing !!YOUR_RESOURCE_KEY!! below.

resourceKey = "!!YOUR_RESOURCE_KEY!!"

if resourceKey == "!!YOUR_RESOURCE_KEY!!":
    print("""
    You need to create a resource key at
    https://configure.51degrees.com and paste it into the code,
    'replacing !!YOUR_RESOURCE_KEY!!
    To get a resourcekey with the properties used in this example go to https://configure.51degrees.com/fzzSBD8R
    """)
else:

    # Here we add some callback settings for the page to make a request with extra evidence from the client side, in this case the Flask /json route we will make below

    javascriptBuilderSettings = {
        "endpoint": "/json"
    }

    pipeline = DeviceDetectionPipelineBuilder({"resourceKey": resourceKey, "javascriptBuilderSettings": javascriptBuilderSettings}).build()
    
    from flask import Flask, request

    app = Flask(__name__)

    # First we make a JSON route that will be called from the client side and will return
    # a JSON encoded property database using any additional evidence provided by the client 

    @app.route('/json', methods=['POST'])
    def jsonroute():

        # Create the flowData object for the JSON route
        flowData = pipeline.createFlowData()

        # Add any information from the request (headers, cookies and additional 
        # client side provided information)

        flowData.evidence.setFromDict(webevidence(request))

        # Process the flowData

        flowData.process()

        # Return the JSON from the JSONBundler engine

        return json.dumps(flowData.jsonbundler.json)

    # Helper function to get a property value if it exists and return 
    # the reason why if it doesn't
    def getValueHelper(flowdata, engine, propertyKey):

        engineProperties = getattr(flowdata, engine)

        propertyValue = getattr(engineProperties, propertyKey)

        if propertyValue.hasValue():
            return propertyValue.value()
        else:
            return propertyValue.noValueMessage

    # In the main route we dynamically update the screen's device property display
    # using the above JSON route

    @app.route('/')
    def server():

        # Create the flowData object for the JSON route
        flowData = pipeline.createFlowData()

        # Add any information from the request (headers, cookies and additional 
        # client side provided information)

        flowData.evidence.setFromDict(webevidence(request))

        # Process the flowData

        flowData.process()

        # Generate the HTML

        output = "<h1>Client side evidence</h1>"

        # Add the JavaScript created by the pipeline
        output += "<script>"
        output += flowData.javascriptbuilder.javascript
        output += "</script>"

        # Print results from server side processing
        output += "<p><b>The following values are determined by sever-side device detection on the first request:</b></p>"

        output += "<b>Hardware Vendor:</b> " + getValueHelper(flowData, "device", "hardwarevendor")
        output += "<br />"
        output += "<b>Hardware Name:</b> " + str(getValueHelper(flowData, "device", "hardwarename"))
        output += "<br />"
        output += "<b>Device Type:</b> " + getValueHelper(flowData, "device", "devicetype")
        output += "<br />"
        output += "<b>Platform Vendor:</b> " + getValueHelper(flowData, "device", "platformvendor")
        output += "<br />"
        output += "<b>Platform Name:</b> " + getValueHelper(flowData, "device", "platformname")
        output += "<br />"
        output += "<b>Browser Vendor:</b> " + getValueHelper(flowData, "device", "browservendor")
        output += "<br />"
        output += "<b>Browser Name:</b> " + getValueHelper(flowData, "device", "browsername")
        output += "<br />"
        output += "<b>Browser Version:</b> " + getValueHelper(flowData, "device", "browserversion")
        output += "<br />"
        output += "<b>Screen width (pixels):</b> " + str(getValueHelper(flowData, "device", "screenpixelswidth"))
        output += "<br />"
        output += "<b>Screen height (pixels):</b> " + str(getValueHelper(flowData, "device", "screenpixelsheight"))
     
        ## Print results of client side processing to the page.
        output += """

        <p>The information shown below is determined from JavaScript running on the client-side that is able to obtain additional evidence. If no additional information appears then it may indicate an external problem such as JavaScript being disabled in your browser.</p>

        <p>Note that the 'Hardware Name' field is intended to illustrate detection of Apple device models as this cannot be determined server-side. This can be tested to some extent using most emulators such as those in the 'developer tools' menu in Google Chrome. However, using real devices will result in more precise model numbers.</p>

              <p id=hardwarename></p>
              <p id=screenpixelwidth></p>
              <p id=screenpixelheight></p>
              <script>
              window.onload = function(){
                fod.complete(function (data) {
                      if(data.device["hardwarename"]){
                      document.getElementById('hardwarename').innerHTML = "<strong>Updated Hardware Name from client-side evidence:</strong> " + data.device["hardwarename"];
                      }
                      document.getElementById('screenpixelwidth').innerHTML = "<strong>Screen width (pixels): " + data.device.screenpixelswidth + "</strong>"
                      document.getElementById('screenpixelheight').innerHTML = "<strong>Screen height (pixels): " + data.device.screenpixelsheight + "</strong>"
                    });
              }
              </script>
        """

        return output
