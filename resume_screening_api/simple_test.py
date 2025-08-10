#!/usr/bin/env python3

import sys
import os
import urllib.request
import urllib.parse
import json

def test_predict_api():
    url = "http://127.0.0.1:5000/predict"
    
    # Test data
    data = {
        'resume_text': '''
        John Doe
        Data Scientist
        
        Skills:
        - Python programming
        - Machine Learning with scikit-learn
        - Data analysis with pandas and numpy
        - Data visualization with matplotlib
        - Statistical analysis
        
        Experience:
        - 3 years in data science
        - Built predictive models
        - Worked with large datasets
        '''
    }
    
    # Encode data
    data_encoded = urllib.parse.urlencode(data).encode('utf-8')
    
    try:
        # Create request
        req = urllib.request.Request(url, data=data_encoded, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        
        # Send request
        print("Sending request...")
        with urllib.request.urlopen(req) as response:
            result = response.read().decode('utf-8')
            print(f"Status Code: {response.getcode()}")
            print(f"Response: {result}")
            
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
        error_response = e.read().decode('utf-8')
        print(f"Error Response: {error_response}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_predict_api()
