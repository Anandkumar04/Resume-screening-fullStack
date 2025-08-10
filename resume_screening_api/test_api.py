import requests
import json

# Test the Flask app
url = "http://127.0.0.1:5000/predict"

# Test with sample resume text
test_resume = """
John Doe
Software Developer
Email: john.doe@email.com

Experience:
- 3 years of Python development
- Experience with Flask, Django
- Machine Learning projects using scikit-learn
- Data analysis with pandas and numpy
- Web development with HTML, CSS, JavaScript

Skills:
- Python, Java, JavaScript
- Machine Learning, Data Science
- Web Development
- Database management
"""

# Test POST request
data = {
    'resume_text': test_resume
}

try:
    response = requests.post(url, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
