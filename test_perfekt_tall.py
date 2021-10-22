# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:28:39 2021

@author: Eier
"""

import unittest
from eksempel_for_testing import delelig, perfekt

class TestDelelig(unittest.TestCase):
    def test_delelig(self):
        self.assertTrue(delelig(6, 2))
        self.assertFalse(delelig(8, 3))
        self.assertTrue(delelig(6, 3))
        self.assertTrue(delelig(9, 3))
        self.assertTrue(delelig(100, 2))
        self.assertFalse(delelig(9, 2))
        
    
    def test_perfekt(self):
        self.assertTrue(perfekt(6))
        self.assertFalse(perfekt(10))
        self.assertTrue(perfekt(28))
        self.assertTrue(perfekt(497))   
        self.assertFalse(perfekt(53))
        self.assertFalse(perfekt(79))
    
if __name__ == "__main__":
    unittest.main()