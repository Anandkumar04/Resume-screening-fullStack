import pickle
import numpy as np
import os
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

def load_model():
    """
    Load the trained model, vectorizer, and label encoder
    
    Returns:
        tuple: (model, vectorizer, label_encoder)
    """
    model_path = 'models/resume_classifier.pkl'
    vectorizer_path = 'models/tfidf_vectorizer.pkl'
    encoder_path = 'models/label_encoder.pkl'
    
    if not all(os.path.exists(path) for path in [model_path, vectorizer_path, encoder_path]):
        raise FileNotFoundError("Model files not found. Please train the model first.")
    
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    with open(vectorizer_path, 'rb') as f:
        vectorizer = pickle.load(f)
        
    with open(encoder_path, 'rb') as f:
        label_encoder = pickle.load(f)
    
    return model, vectorizer, label_encoder

def predict_category(resume_text, model, vectorizer, label_encoder):
    """
    Predict the category of a resume
    
    Args:
        resume_text (str): Cleaned resume text
        model: Trained classifier model
        vectorizer: Fitted TF-IDF vectorizer
        label_encoder: Fitted label encoder
    
    Returns:
        tuple: (predicted_category, confidence_score)
    """
    # Transform text to TF-IDF features
    text_features = vectorizer.transform([resume_text])
    
    # Make prediction
    prediction = model.predict(text_features)[0]
    prediction_proba = model.predict_proba(text_features)[0]
    
    # Get category name
    category = label_encoder.inverse_transform([prediction])[0]
    
    # Get confidence (max probability)
    confidence = np.max(prediction_proba)
    
    return category, confidence

def save_model(model, vectorizer, label_encoder):
    """
    Save the trained model, vectorizer, and label encoder
    
    Args:
        model: Trained classifier model
        vectorizer: Fitted TF-IDF vectorizer
        label_encoder: Fitted label encoder
    """
    os.makedirs('models', exist_ok=True)
    
    with open('models/resume_classifier.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    with open('models/tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
        
    with open('models/label_encoder.pkl', 'wb') as f:
        pickle.dump(label_encoder, f)
    
    print("Model saved successfully!")
