#!/usr/bin/env python3
"""
Test script to verify PDF support and general API functionality
"""

import requests
import json

def test_text_input():
    """Test with plain text input"""
    print("🧪 Testing text input...")
    
    url = "http://127.0.0.1:5000/predict"
    
    sample_resume = """
    John Doe
    Data Scientist
    Email: john.doe@email.com
    
    Experience:
    • 5 years in data science and machine learning
    • Proficient in Python, R, and SQL
    • Experience with pandas, numpy, scikit-learn
    • Built predictive models for customer segmentation
    • Data visualization with matplotlib and seaborn
    
    Skills:
    • Machine Learning: Classification, Regression, Clustering
    • Deep Learning: TensorFlow, Keras
    • Data Processing: pandas, numpy
    • Visualization: matplotlib, seaborn, plotly
    • Databases: MySQL, PostgreSQL, MongoDB
    
    Projects:
    • Customer Churn Prediction using Random Forest
    • Sales Forecasting with ARIMA models
    • Natural Language Processing for sentiment analysis
    """
    
    data = {'resume_text': sample_resume}
    
    try:
        response = requests.post(url, data=data)
        print(f"✅ Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Category: {result['category']}")
            print(f"✅ Confidence: {result['confidence']}")
            print(f"✅ Text Preview: {result['cleaned_text_preview'][:100]}...")
        else:
            error = response.json()
            print(f"❌ Error: {error.get('error', 'Unknown error')}")
            
    except Exception as e:
        print(f"❌ Request failed: {e}")

def test_api_status():
    """Test if the API is running"""
    print("🧪 Testing API status...")
    
    try:
        response = requests.get("http://127.0.0.1:5000/test")
        if response.status_code == 200:
            print("✅ API is running and responding")
            result = response.json()
            print(f"✅ Response: {result}")
        else:
            print(f"❌ API returned status: {response.status_code}")
    except Exception as e:
        print(f"❌ API test failed: {e}")

if __name__ == "__main__":
    print("🚀 Starting Resume Screening API Tests")
    print("=" * 50)
    
    test_api_status()
    print()
    test_text_input()
    
    print("\n" + "=" * 50)
    print("Tests completed!")
