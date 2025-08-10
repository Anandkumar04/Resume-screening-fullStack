"""
Retrain the model with Full Stack Developer category included
"""
import pandas as pd
import numpy as np
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

def clean_resume(resume_text):
    """Clean and preprocess resume text"""
    # Remove URLs
    resume_text = re.sub(r'http\S+', '', resume_text)
    
    # Remove RT and cc
    resume_text = re.sub(r'RT|cc', '', resume_text)
    
    # Remove hashtags
    resume_text = re.sub(r'#\S+', '', resume_text)
    
    # Remove mentions
    resume_text = re.sub(r'@\S+', '', resume_text)
    
    # Remove punctuation
    resume_text = resume_text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespaces
    resume_text = re.sub(r'\s+', ' ', resume_text)
    
    # Convert to lowercase
    resume_text = resume_text.lower().strip()
    
    # Remove stopwords and lemmatize
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    words = resume_text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    
    return ' '.join(words)

def retrain_with_fullstack():
    print("Loading dataset...")
    
    # Try to load updated dataset first, fallback to original
    try:
        df = pd.read_csv('../resume_dataset_updated.csv')
        print("Using updated dataset with Full Stack category")
    except:
        df = pd.read_csv('../resume_dataset.csv')
        print("Using original dataset - Full Stack category may not be available")
    
    print(f"Dataset loaded with {len(df)} resumes")
    print(f"Categories found: {len(df['Category'].unique())}")
    print("\nCategory distribution:")
    print(df['Category'].value_counts().head(10))
    
    print("\nCleaning resume texts...")
    df['cleaned_resume'] = df['Resume'].apply(clean_resume)
    
    print("Preparing features and labels...")
    X = df['cleaned_resume'].values
    y = df['Category'].values
    
    # Encode labels
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    
    print(f"\nTraining on {len(label_encoder.classes_)} categories:")
    for i, category in enumerate(label_encoder.classes_):
        count = sum(y == category)
        print(f"{i+1}. {category}: {count} samples")
    
    print("\nCreating TF-IDF features...")
    vectorizer = TfidfVectorizer(
        sublinear_tf=True,
        stop_words='english',
        max_features=2000,  # Increased for better full-stack detection
        ngram_range=(1, 2)  # Include bigrams for better context
    )
    
    X_features = vectorizer.fit_transform(X)
    print(f"Created {X_features.shape[1]} features")
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X_features, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )
    
    print(f"Training set: {X_train.shape[0]} samples")
    print(f"Test set: {X_test.shape[0]} samples")
    
    # Train the model with optimized parameters for full-stack detection
    print("\nTraining KNN classifier...")
    model = KNeighborsClassifier(
        n_neighbors=7,  # Slightly increased for better generalization
        weights='distance',  # Give more weight to closer neighbors
        algorithm='auto'
    )
    
    model.fit(X_train, y_train)
    
    # Evaluate the model
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nModel Accuracy: {accuracy:.4f}")
    
    # Save the retrained model and components
    print("\nSaving retrained model...")
    joblib.dump(model, 'models/resume_classifier_updated.pkl')
    joblib.dump(vectorizer, 'models/tfidf_vectorizer_updated.pkl')
    joblib.dump(label_encoder, 'models/label_encoder_updated.pkl')
    
    print("✅ Model retrained and saved successfully!")
    print("\nTo use the updated model, modify your app.py to load:")
    print("- models/resume_classifier_updated.pkl")
    print("- models/tfidf_vectorizer_updated.pkl")
    print("- models/label_encoder_updated.pkl")
    
    return accuracy, label_encoder.classes_

if __name__ == "__main__":
    try:
        accuracy, categories = retrain_with_fullstack()
        print(f"\n🎯 Model retrained with {accuracy:.2%} accuracy!")
        print(f"📋 Available categories: {list(categories)}")
    except Exception as e:
        print(f"❌ Error during retraining: {e}")
        import traceback
        traceback.print_exc()
