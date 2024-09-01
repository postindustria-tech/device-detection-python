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

import flask_unittest
import unittest
from fiftyone_pipeline_core.logger import Logger
from fiftyone_devicedetection_examples.example_utils import ExampleUtils
from fiftyone_devicedetection_examples.onpremise.gettingstarted_web.app import GettingStartedWeb

class OnPremiseGettingStartedWebTests(flask_unittest.ClientTestCase):
    # Assign the `Flask` app object
    #data_file = ExampleUtils.find_file("51Degrees-LiteV4.1.hash")

    user_agents_file = ExampleUtils.find_file("20000 User Agents.csv")
    logger = Logger()
    config = GettingStartedWeb.build_config()
    app = GettingStartedWeb().build(config, logger).app

    def test_onpremise_getting_started_web(self, client):
        response = client.get('/')
        self.assertEqual(200, response.status_code)
