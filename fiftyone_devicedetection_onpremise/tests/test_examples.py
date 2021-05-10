import os
import unittest

class DeviceDetectionExampleTests(unittest.TestCase):

    def test_hash_getting_started(self):
        
        import examples.hash.gettingstarted

    def test_hash_failure_to_match(self):
        
        import examples.hash.failuretomatch

    def test_hash_match_metrics(self):
        
        import examples.hash.match_metrics

    def test_hash_metadata(self):
        
        import examples.hash.metadata

    def test_hash_offline_processing(self):

        # Only run if environment variable set

        if "run_performance_tests" in os.environ:

            import examples.hash.offline_processing

    def test_hash_performance(self):

        # Only run if environment variable set

        if "run_performance_tests" in os.environ:
            
            import examples.hash.performance


