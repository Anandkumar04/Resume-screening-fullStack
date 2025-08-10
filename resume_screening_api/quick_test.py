#!/usr/bin/env python3

import urllib.request
import urllib.parse
import json

def test_predict():
    """Test the predict endpoint with sample data"""
    url = "http://127.0.0.1:5000/predict"
    
    # Sample resume text
    sample_resume = """
    John Smith
    Software Engineer
    
    Experience:
    - 3+ years in Python development
    - Machine learning with scikit-learn and pandas
    - Web development using Flask and Django
    - Data analysis and visualization
    - SQL database management
    
    Skills:
    - Programming: Python, Java, JavaScript
    - Machine Learning: scikit-learn, pandas, numpy
    - Web: HTML, CSS, React, Flask
    - Databases: MySQL, PostgreSQL
    - Tools: Git, Docker, AWS
    
    Education:
    Bachelor of Computer Science
    """
    
    # Prepare form data
    data = {'resume_text': sample_resume}
    data_encoded = urllib.parse.urlencode(data).encode('utf-8')
    
    try:
        print("Testing /predict endpoint...")
        print(f"Sending data length: {len(data_encoded)} bytes")
        
        # Create and send request
        req = urllib.request.Request(url, data=data_encoded, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        
        with urllib.request.urlopen(req) as response:
            result = response.read().decode('utf-8')
            print(f"✅ Success! Status: {response.getcode()}")
            print(f"Response: {json.loads(result)}")
            
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error: {e.code}")
        error_response = e.read().decode('utf-8')
        try:
            error_data = json.loads(error_response)
            print(f"Error details: {error_data}")
        except:
            print(f"Raw error: {error_response}")
            
    except Exception as e:
        print(f"❌ Network Error: {e}")

if __name__ == "__main__":
    test_predict()
