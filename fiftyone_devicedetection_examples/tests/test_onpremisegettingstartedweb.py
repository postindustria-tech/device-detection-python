import logging
import flask_unittest
from fiftyone_devicedetection_examples.example_utils import ExampleUtils
from fiftyone_devicedetection_examples.onpremise.gettingstarted_web.app import GettingStartedWeb

class OnPremiseGettingStartedWebTests(flask_unittest.ClientTestCase):
    # Assign the `Flask` app object
    data_file = ExampleUtils.find_file("51Degrees-LiteV4.1.hash")
    user_agents_file = ExampleUtils.find_file("20000 User-Agents.csv")
    logger = logging.getLogger("Hash Example Tests")
    app = GettingStartedWeb().build(data_file).app

    def test_onpremise_getting_started_web(self, client):
        response = client.get('/')
        self.assertEqual(200, response.status_code)
