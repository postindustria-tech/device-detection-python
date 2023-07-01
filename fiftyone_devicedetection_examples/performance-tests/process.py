# *********************************************************************
# This Original Work is copyright of 51 Degrees Mobile Experts Limited.
# Copyright 2023 51 Degrees Mobile Experts Limited, Davidson House,
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


## @performance-tests/process.py

from fiftyone_devicedetection_onpremise.devicedetection_onpremise_pipelinebuilder import DeviceDetectionOnPremisePipelineBuilder
from fiftyone_pipeline_core.web import webevidence
import json

# First create the device detection pipeline with the desired settings.
data_file = "../../fiftyone_devicedetection_onpremise/cxx/device-detection-data/51Degrees-LiteV4.1.hash"

# Create Device Detection pipeline using datafile
pipeline = DeviceDetectionOnPremisePipelineBuilder(
    data_file_path = data_file, 
    licence_keys = "", 
    performance_profile = 'MaxPerformance', 
    update_on_start=False).build()

from flask import Flask, request
app = Flask(__name__)

# Helper function to get a property value if it exists and return 
# the reason why if it doesn't
def getValueHelper(flowdata, engine, propertyKey):

    engineProperties = getattr(flowdata, engine)

    try:
        propertyValue = getattr(engineProperties, propertyKey)

        if propertyValue.has_value():
            return propertyValue.value()
        else:
            return propertyValue.no_value_message()
    except:
        return "Not found in datafile"

@app.route('/')
@app.route('/calibrate')
def calibrateRoute():
    output = "<h2>Calibrate Example</h2><br/>\n" 
    return output

@app.route('/process')
def processRoute():
    # Create the flowdata object for the JSON route
    flowdata = pipeline.create_flowdata()

    # Add any information from the request (headers, cookies and additional 
    # client side provided information)
    flowdata.evidence.add_from_dict(webevidence(request))

    # Process the flowdata
    flowdata.process()
    
    # Generate the HTML
    output = "<h2>Process Example</h2><br/>\n" 
    output += "<b>Is Mobile:</b> " + str(getValueHelper(flowdata, "device", "ismobile"))
    output += "<br />"

    return output

if __name__ == "__main__":
    app.run()