'''
Created on 6/10/2011

@author: dave
'''
import os
import unittest

from badcollage import build

class TestBuilder(unittest.TestCase):


    def setUp(self):
        self.b = build.Builder()
        self.base_dir = os.path.dirname(os.path.abspath(__file__))        

    def tearDown(self):
        pass


    def test_build_from_mixed_sourcedir(self):
        mixed_source_dir = os.path.join(self.base_dir, "mixed_source")
        _orig_source = self.b.source_dir
        self.b.source_dir = mixed_source_dir
        imgs = self.b.get_source_imgs() 
        for img in imgs:
            assert img.format

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()