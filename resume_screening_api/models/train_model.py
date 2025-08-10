import pandas as pd
import numpy as np
import pickle
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import sys
import os

def clean_resume(resume_text):
    """Clean resume text by removing URLs, mentions, hashtags, punctuation, and extra whitespace."""
    resume_text = re.sub(r'http\S+\s*', ' ', resume_text)
    resume_text = re.sub('RT|cc', ' ', resume_text)
    resume_text = re.sub(r'#\S+', '', resume_text)
    resume_text = re.sub(r'@\S+', '  ', resume_text)
    # Remove punctuation
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for p in punctuation:
        resume_text = resume_text.replace(p, ' ')
    resume_text = re.sub(r'[^\x00-\x7f]', r' ', resume_text) 
    resume_text = re.sub(r'\s+', ' ', resume_text)
    return resume_text.strip()

def save_model(model, vectorizer, label_encoder):
    """Save the trained model, vectorizer, and label encoder"""
    os.makedirs('models', exist_ok=True)
    
    with open('models/resume_classifier.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    with open('models/tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
        
    with open('models/label_encoder.pkl', 'wb') as f:
        pickle.dump(label_encoder, f)
    
    print("Model saved successfully!")

def train_and_save_model():
    """
    Train the resume classification model and save it
    
    Returns:
        float: Model accuracy on test set
    """
    print("Loading dataset...")
    # Load the dataset - looking in parent directory
    dataset_path = os.path.join('..', 'resume_dataset.csv')
    if not os.path.exists(dataset_path):
        print(f"Dataset not found at {dataset_path}")
        return 0.0
        
    df = pd.read_csv(dataset_path, encoding='utf-8')
    print(f"Loaded {len(df)} resume records")
    
    print("Cleaning resume texts...")
    # Clean resume texts
    df['cleaned_resume'] = df['Resume'].apply(clean_resume)
    
    print("Preparing features and labels...")
    # Prepare features and labels
    X = df['cleaned_resume'].values
    y = df['Category'].values
    
    # Encode labels
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    
    print(f"Found {len(label_encoder.classes_)} categories: {label_encoder.classes_}")
    
    print("Creating TF-IDF features...")
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(
        sublinear_tf=True,
        stop_words='english',
        max_features=1500
    )
    
    # Fit and transform text to TF-IDF features
    X_tfidf = vectorizer.fit_transform(X)
    
    print("Splitting data...")
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X_tfidf, y_encoded, 
        test_size=0.2, 
        random_state=42,
        stratify=y_encoded
    )
    
    print(f"Training set: {X_train.shape[0]} samples")
    print(f"Test set: {X_test.shape[0]} samples")
    
    print("Training model...")
    # Train model
    model = OneVsRestClassifier(KNeighborsClassifier(n_neighbors=5))
    model.fit(X_train, y_train)
    
    print("Evaluating model...")
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))
    
    print("Saving model...")
    # Save model, vectorizer, and label encoder
    save_model(model, vectorizer, label_encoder)
    
    return accuracy

if __name__ == "__main__":
    train_and_save_model()
