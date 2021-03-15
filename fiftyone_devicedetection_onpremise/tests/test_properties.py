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

import os
import unittest

from fiftyone_pipeline_core.pipelinebuilder import PipelineBuilder
from fiftyone_devicedetection_onpremise.devicedetection_onpremise import DeviceDetectionOnPremise
from fiftyone_devicedetection_shared.utils import *

data_file = "./fiftyone_devicedetection_onpremise/device-detection-cxx/device-detection-data/51Degrees-LiteV4.1.hash"
mobile_ua = ("Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) "
            "AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile"
            "/11D167 Safari/9537.53")

# Create a simple pipeline to access the engine with and process it with flow data
deviceDetectionOnPremiseEngine = DeviceDetectionOnPremise(
            data_file_path = data_file, 
            licence_keys = "",
            auto_update=False)
pipeline = PipelineBuilder() \
            .add(deviceDetectionOnPremiseEngine) \
            .build()

class PropertyTests(unittest.TestCase):

    def test_available_properties(self):

        """!
        Tests whether the all the properties present in the engine when initialised with a resource key are accessible.
        """

        flowData = pipeline.create_flowdata()
        flowData.evidence.add("header.user-agent", mobile_ua)
        flowData.process()
        device = flowData.device

        # Get list of all the properties in the engine
        properties_list = deviceDetectionOnPremiseEngine.get_properties()

        # Run test checks on all the properties available in data file
        for propertykey, propertymeta in properties_list.items():
            property = propertymeta["name"]
            dd_property_value = device[property]
            self.assertIsNotNone("Property: " + property +" is not present in the results.", dd_property_value)
            if(dd_property_value.has_value()):
                self.assertNotEquals(property + ".value should not be null", dd_property_value.value(), "noValue")
                self.assertIsNotNone(property + ".value should not be null", dd_property_value.value())
            else:
                self.assertIsNotNone(property + ".noValueMessage should not be null", dd_property_value.no_value_message())
    
    def test_value_types(self):

        """!
        Tests value types of the properties present present in the engine 
        """

        flowData = pipeline.create_flowdata()
        flowData.evidence.add("header.user-agent", mobile_ua)
        flowData.process()
        device = flowData.device

        # Get list of all the properties in the engine
        properties_list = deviceDetectionOnPremiseEngine.get_properties()

        # Run test check valuetypes of properties
        for propertykey, propertymeta in properties_list.items():
            # Engine properties
            property = propertymeta["name"]
            expected_type = propertymeta["type"]

            # Flowdata properties
            dd_property_value = device[property]
            value = dd_property_value.value()
            self.assertIsNotNone("Property: " + property +" is not present in the results.", dd_property_value)
            self.assertTrue("Expected type for " + property + " is " + expected_type + 
            " but actual type is " + get_value_type(value), is_same_type(value, expected_type))



