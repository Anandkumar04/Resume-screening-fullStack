#!/usr/bin/env python3

import pickle
import os
import re

def test_model_loading():
    """Test if we can load and use the model directly"""
    print("Testing model loading...")
    
    # Test model files exist
    model_files = [
        'models/resume_classifier.pkl',
        'models/tfidf_vectorizer.pkl', 
        'models/label_encoder.pkl'
    ]
    
    for file_path in model_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} exists")
        else:
            print(f"❌ {file_path} missing")
            return False
    
    # Load models
    try:
        with open('models/resume_classifier.pkl', 'rb') as f:
            model = pickle.load(f)
        print("✅ Model loaded")
        
        with open('models/tfidf_vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
        print("✅ Vectorizer loaded")
            
        with open('models/label_encoder.pkl', 'rb') as f:
            label_encoder = pickle.load(f)
        print("✅ Label encoder loaded")
        
        # Test text cleaning
        def clean_resume(resume_text):
            resume_text = re.sub(r'http\S+\s*', ' ', resume_text)
            resume_text = re.sub('RT|cc', ' ', resume_text)
            resume_text = re.sub(r'#\S+', '', resume_text)
            resume_text = re.sub(r'@\S+', '  ', resume_text)
            punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            for p in punctuation:
                resume_text = resume_text.replace(p, ' ')
            resume_text = re.sub(r'[^\x00-\x7f]', r' ', resume_text) 
            resume_text = re.sub(r'\s+', ' ', resume_text)
            return resume_text.strip()
        
        # Test prediction
        test_text = "Python developer with experience in machine learning and data science"
        cleaned_text = clean_resume(test_text)
        print(f"✅ Text cleaning works: '{cleaned_text[:50]}...'")
        
        # Transform and predict
        text_features = vectorizer.transform([cleaned_text])
        print("✅ Text vectorization works")
        
        prediction = model.predict(text_features)[0]
        prediction_proba = model.predict_proba(text_features)[0]
        print("✅ Model prediction works")
        
        category = label_encoder.inverse_transform([prediction])[0]
        confidence = max(prediction_proba)
        
        print(f"✅ Test prediction: {category} ({confidence:.2%} confidence)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_model_loading()
    if success:
        print("\n🎉 All model components are working!")
    else:
        print("\n💥 There are issues with model loading/prediction")
