"""
Test PDF processing functionality for deployment debugging
"""
import sys
import os

print("🔍 Testing PDF Processing Dependencies...")
print("="*50)

# Test PyPDF2 import
try:
    import PyPDF2
    print("✅ PyPDF2: Successfully imported")
    print(f"   Version: {PyPDF2.__version__ if hasattr(PyPDF2, '__version__') else 'Unknown'}")
except ImportError as e:
    print(f"❌ PyPDF2: Import failed - {e}")

# Test pdfplumber import  
try:
    import pdfplumber
    print("✅ pdfplumber: Successfully imported")
    print(f"   Version: {pdfplumber.__version__ if hasattr(pdfplumber, '__version__') else 'Unknown'}")
except ImportError as e:
    print(f"❌ pdfplumber: Import failed - {e}")

# Test python-docx import
try:
    from docx import Document
    print("✅ python-docx: Successfully imported")
except ImportError as e:
    print(f"❌ python-docx: Import failed - {e}")

# Test other critical imports
print("\n🔍 Testing Other Dependencies...")
print("-"*30)

try:
    import flask
    print(f"✅ Flask: {flask.__version__}")
except ImportError as e:
    print(f"❌ Flask: {e}")

try:
    import pandas
    print(f"✅ Pandas: {pandas.__version__}")
except ImportError as e:
    print(f"❌ Pandas: {e}")

try:
    import sklearn
    print(f"✅ Scikit-learn: {sklearn.__version__}")
except ImportError as e:
    print(f"❌ Scikit-learn: {e}")

try:
    import nltk
    print(f"✅ NLTK: {nltk.__version__}")
except ImportError as e:
    print(f"❌ NLTK: {e}")

print("\n" + "="*50)
print("📋 Dependency Test Complete!")

# Test if model files exist
print("\n🤖 Checking Model Files...")
print("-"*25)

model_files = [
    'models/resume_classifier.pkl',
    'models/tfidf_vectorizer.pkl', 
    'models/label_encoder.pkl'
]

for model_file in model_files:
    if os.path.exists(model_file):
        size_mb = os.path.getsize(model_file) / (1024*1024)
        print(f"✅ {model_file} ({size_mb:.1f} MB)")
    else:
        print(f"❌ {model_file} - Not found!")

print("\n✅ Dependency check complete!")
print("If all dependencies show ✅, your app should work on Render!")
