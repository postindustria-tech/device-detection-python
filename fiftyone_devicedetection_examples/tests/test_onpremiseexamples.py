import logging
import os
import unittest
from fiftyone_devicedetection_examples.example_utils import ExampleUtils
from fiftyone_devicedetection_examples.onpremise.gettingstarted_console import GettingStartedConsole

class DeviceDetectionExampleTests(unittest.TestCase):

    # Init method - Set data file for hash examples and aditionally a
    # User-Agents file for the performance example.
    def setUp(self):
        self.data_file = ExampleUtils.find_file("51Degrees-LiteV4.1.hash")
        self.user_agents_file = ExampleUtils.find_file("20000 User-Agents.csv")
        self.logger = logging.getLogger("Hash Example Tests")

    def test_onpremise_getting_started_console(self):
        example = GettingStartedConsole()
        example.run(self.data_file, self.logger)

    def test_onpremise_failure_to_match(self):
        
        import fiftyone_devicedetection_examples.onpremise.failuretomatch

    def test_onpremise_match_metrics(self):
        
        import fiftyone_devicedetection_examples.onpremise.match_metrics

    def test_onpremise_metadata(self):
        
        import fiftyone_devicedetection_examples.onpremise.metadata

    def test_onpremise_offline_processing(self):

        # Only run if environment variable set

        if "run_performance_tests" in os.environ:

            import fiftyone_devicedetection_examples.onpremise.offline_processing

    def test_onpremise_performance(self):

        # Only run if environment variable set

        if "run_performance_tests" in os.environ:
            
            import fiftyone_devicedetection_examples.onpremise.performance
