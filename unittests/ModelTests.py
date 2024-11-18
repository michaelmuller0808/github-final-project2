#!/usr/bin/env python
"""
model tests
"""

import sys, os
import unittest
sys.path.insert(1, os.path.join('..', os.getcwd()))

## import model specific functions and variables
from model import *




class ModelTest(unittest.TestCase):
    """
    test the essential functionality
    """
        
    def test_01_train(self):
        """
        test the train functionality
        """

        ## train the model
        data_dir = os.path.join("data","cs-train")
        model_train(data_dir,test=True)

    def test_02_load(self):
        """
        test the train functionality
        """
                        
        ## train the model
        all_data, all_models = model_load()

       
    def test_03_predict(self):
        """
        test the predict function input
        """

        ## load model first
        all_data, all_models = model_load()
    
        ## ensure that a list can be passed
        country='all'
        year='2018'
        month='01'
        day='05'
        result = model_predict(country,year,month,day)
        print(result)

          
### Run the tests
if __name__ == '__main__':
    unittest.main()
