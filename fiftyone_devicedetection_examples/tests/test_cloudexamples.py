import inspect
import json5
from pathlib import Path
import unittest
from fiftyone_devicedetection_examples.cloud.nativemodellookup_console import NativeModelLookupConsole
from fiftyone_devicedetection_examples.cloud.taclookup_console import TacLookupConsole
from fiftyone_pipeline_core.logger import Logger
from fiftyone_devicedetection_examples.example_utils import ExampleUtils
from fiftyone_devicedetection_examples.cloud.gettingstarted_console import GettingStartedConsole

class DeviceDetectionExampleTests(unittest.TestCase):

    # Init method - specify Resource Key to run examples here or 
    # set a Resource Key in an environment variable called 'resource_key'.
    def setUp(self):
        self.resource_key = ExampleUtils.get_resource_key()
        self.logger = Logger()

        if not self.resource_key:
            self.fail(
                "ResourceKey must be specified in the setUp method" +
                " or as an Environment variable")

    def test_cloud_getting_started_console(self):
        example = GettingStartedConsole()
        configFile = Path(inspect.getfile(example.__class__)).parent.resolve().joinpath("gettingstarted_console.json").read_text()
        config = json5.loads(configFile)
        ExampleUtils.set_resource_key_in_config(config, self.resource_key)
        example.run(config, self.logger, print)
    def test_cloud_nativemodellookup_console(self):
        example = NativeModelLookupConsole()
        example.run(self.resource_key, self.logger, print)
    def test_cloud_taclookup_console(self):
        example = TacLookupConsole()
        configFile = Path(inspect.getfile(example.__class__)).parent.resolve().joinpath("taclookup_console.json").read_text()
        config = json5.loads(configFile)
        ExampleUtils.set_resource_key_in_config(config, self.resource_key)
        example.run(config, self.logger, print)
