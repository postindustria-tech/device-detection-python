import os
import unittest

class DeviceDetectionExampleTests(unittest.TestCase):
    def test_cloud_getting_started(self):
        if "resource_key" in os.environ:    
            import examples.cloud.gettingstarted

    def test_cloud_failure_to_match(self):
        if "resource_key" in os.environ:
            import examples.cloud.failuretomatch
			
    def test_cloud_useragentclienthints(self):
        if "resource_key" in os.environ:    
            import examples.cloud.useragentclienthints
			
    def test_cloud_metadata(self):
        if "resource_key" in os.environ:
            import examples.cloud.metadata

    def test_cloud_nativemodellookup(self):

        if "resource_key" in os.environ:
            import examples.cloud.nativemodellookup
