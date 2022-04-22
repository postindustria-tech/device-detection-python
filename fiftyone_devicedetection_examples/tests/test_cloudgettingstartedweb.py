import flask_unittest
from fiftyone_pipeline_core.logger import Logger
from fiftyone_devicedetection_examples.example_utils import ExampleUtils
from fiftyone_devicedetection_examples.cloud.gettingstarted_web.app import GettingStartedWeb

class CloudGettingStartedWebTests(flask_unittest.ClientTestCase):
    # Assign the `Flask` app object
    resource_key = ExampleUtils.get_resource_key()
    logger = Logger()
    app = GettingStartedWeb().build(resource_key, logger).app

    def test_cloud_getting_started_web(self, client):
        response = client.get('/')
        self.assertEqual(200, response.status_code)
