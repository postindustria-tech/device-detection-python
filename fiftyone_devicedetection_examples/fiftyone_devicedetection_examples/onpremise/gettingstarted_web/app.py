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


## @example onpremise/gettingstarted_web/app.py
#
# @include{doc} example-getting-started-web.txt
# 
# This example is available in full on [GitHub](https://github.com/51Degrees/device-detection-python/blob/master/fiftyone_devicedetection_examples/fiftyone_devicedetection_examples/onpremise/gettingstarted-web/app.py). 
# 
# @include{doc} example-require-datafile.txt
# 
# Required PyPi Dependencies:
# - fiftyone_devicedetection
# - flask
# 
# ## Overview
# 
# The `DeviceDetectionPipelineBuilder` class is used to create a Pipeline instance from the configuration
# that is supplied.
# The fiftyone_pipeline_core.web module contains helpers which deal with
# automatically populating evidence from a web request.
# ```{py}
# flowdata.evidence.add_from_dict(webevidence(request))
# ```

# The module can also handling setting response headers (e.g. Accept-CH for User-Agent 
# Client Hints) and serving requests for client-side JavaScript and JSON resources.
# ```{py}
# set_response_header(flowdata, response)
# ```
# 
# The results of detection can be accessed by through the flowdata object once
# processed. This can then be used to interrogate the data.
# ```{py}
# flowdata.process()
# device = flowdata.device
# hardware_vendor = device.hardwarevendor
# ```
# 
# Results can also be accessed in client-side code by using the `fod` object. See the 
# [JavaScriptBuilderElementBuilder](https://51degrees.com/pipeline-python/4.3/classpipeline-python_1_1fiftyone__pipeline__core_1_1fiftyone__pipeline__core_1_1javascriptbuilde778a9036818b19ab55d981a40be4a4d7.html)
# for details on available settings such as changing the `fod` name.
# ```{js}
# window.onload = function () {
#     fod.complete(function(data) {
#         var hardwareName = data.device.hardwarename;
#         alert(hardwareName.join(", "));
#     }
# }
# ```
#
# ## View
# @include templates/index.html
#
# ## App

import logging
import sys
from fiftyone_devicedetection_examples.example_utils import ExampleUtils
from flask.helpers import make_response
from flask import Flask, request, render_template
from fiftyone_devicedetection.devicedetection_pipelinebuilder import DeviceDetectionPipelineBuilder
from fiftyone_pipeline_core.web import *
import json

# In this example, by default, the 51degrees "Lite" file needs to be
# somewhere in the project space.
#
# Note that the Lite data file is only used for illustration, and has
# limited accuracy and capabilities.
# Find out about the Enterprise data file on our pricing page:
# https://51degrees.com/pricing
LITE_V_4_1_HASH = "51Degrees-LiteV4.1.hash";


class GettingStartedWeb():
    app = Flask(__name__)

    def build(self, data_file):
        # Here we add some callback settings for the page to make a request with extra evidence from the client side, in this case the Flask /json route we will make below

        javascript_builder_settings = {
            "endpoint": "/json",
            "minify": True,
            # The enable_cookies setting is needed if you want to work with results from client-side
            # evidence on the server. For example, precise Apple models or screen dimensions.
            # This will store the results of client-side detection scripts on the client as cookies.
            # On subsequent requests, these cookies will be included in the payload and will be 
            # used by the device detection API when it runs.
            "enable_cookies": True
        }

        GettingStartedWeb.pipeline = DeviceDetectionPipelineBuilder(
            data_file_path = data_file, 
            # We use the low memory profile as its performance is
            # sufficient for this example. See the documentation for
            # more detail on this and other configuration options:
            # http://51degrees.com/documentation/4.3/_device_detection__features__performance_options.html
            # http://51degrees.com/documentation/4.3/_features__automatic_datafile_updates.html
            # http://51degrees.com/documentation/4.3/_features__usage_sharing.html
            performance_profile = "LowMemory",
            # inhibit sharing usage for this test, usually this
            # should be set "true"
            auto_update = False,
            licence_keys = "",
            javascript_builder_settings = javascript_builder_settings).build()

        return self

    def run(self):
        
        GettingStartedWeb.app.run()

    # First we make a JSON route that will be called from the client side and will return
    # a JSON encoded property database using any additional evidence provided by the client 

    @app.route('/json', methods=['POST'])
    def jsonroute():

        # Create the flowdata object for the JSON route
        flowdata = GettingStartedWeb.pipeline.create_flowdata()

        # Add any information from the request (headers, cookies and additional 
        # client side provided information)

        flowdata.evidence.add_from_dict(webevidence(request))

        # Process the flowdata

        flowdata.process()

        # Return the JSON from the JSONBundler engine

        return json.dumps(flowdata.jsonbundler.json)

    # In the main route we dynamically update the screen's device property display
    # using the above JSON route

    @app.route('/')
    def server():

        # Create the flowdata object for the JSON route
        flowdata = GettingStartedWeb.pipeline.create_flowdata()

        # Add any information from the request (headers, cookies and additional 
        # client side provided information)

        flowdata.evidence.add_from_dict(webevidence(request))

        # Process the flowdata

        flowdata.process()

        response = make_response()

        # Some browsers require that extra HTTP headers are explicitly
        # requested. So set whatever headers are required by the browser in
        # order to return the evidence needed by the pipeline.
        # More info on this can be found at
        # https://51degrees.com/blog/user-agent-client-hints

        set_response_header(flowdata, response)

        # Generate the HTML
        response.set_data(render_template(
            'index.html',
            data=flowdata,
            utils=ExampleUtils,
            response=response))

        return response

def main(argv):
    # Use the supplied path for the data file or find the lite
    # file that is included in the repository.
    data_file = argv[0] if len(argv) > 0 else ExampleUtils.find_file(LITE_V_4_1_HASH)

    # Configure a logger to output to the console.
    logger = logging.getLogger("Getting Started")
    logger.setLevel(logging.INFO)

    if (data_file != None):
        GettingStartedWeb().build(data_file).run()
    else:
        logger.error("Failed to find a device detection " +
            "data file. Make sure the device-detection-data " +
            "submodule has been updated by running " +
            "`git submodule update --recursive`.")

if __name__ == "__main__":
    main(sys.argv[1:])
