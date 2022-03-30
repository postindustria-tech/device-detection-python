import logging
from threading import Thread
import unittest
from fiftyone_devicedetection_examples.example_utils import ExampleUtils
from fiftyone_devicedetection_examples.cloud.gettingstarted_console import GettingStartedConsole

class DeviceDetectionExampleTests(unittest.TestCase):

    # Init method - specify Resource Key to run examples here or 
    # set a Resource Key in an environment variable called 'resource_key'.
    def setUp(self):
        self.resource_key = ExampleUtils.get_resource_key()
        self.logger = logging.getLogger("Cloud Example Tests")

        if not self.resource_key:
            self.fail(
                "ResourceKey must be specified in the setUp method" +
                " or as an Environment variable")

    def test_cloud_getting_started_console(self):
        example = GettingStartedConsole()
        example.run(self.resource_key, self.logger)
