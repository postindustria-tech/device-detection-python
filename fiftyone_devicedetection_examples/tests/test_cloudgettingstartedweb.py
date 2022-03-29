import logging
from threading import Thread
import flask_unittest
from fiftyone_devicedetection_examples.example_utils import ExampleUtils
from fiftyone_devicedetection_examples.cloud.gettingstarted_web.app import GettingStartedWeb

class CloudGettingStartedWebTests(flask_unittest.ClientTestCase):
    # Assign the `Flask` app object
    resource_key = ExampleUtils.get_resource_key()
    logger = logging.getLogger("Cloud Example Tests")
    app = GettingStartedWeb().build(resource_key).app

    def test_cloud_getting_started_web(self, client):
        response = client.get('/')
        self.assertEqual(200, response.status_code)
