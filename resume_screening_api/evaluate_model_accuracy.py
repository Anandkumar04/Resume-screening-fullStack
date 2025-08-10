import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def evaluate_model_accuracy():
    """Comprehensive model accuracy evaluation"""
    
    print("=== RESUME SCREENING MODEL ACCURACY ANALYSIS ===\n")
    
    # 1. Load the dataset
    try:
        df = pd.read_csv('../resume_dataset.csv')
        print(f"✅ Dataset loaded: {len(df)} resumes")
        print(f"📊 Categories: {len(df['Category'].unique())}")
        
        # Show category distribution
        category_counts = df['Category'].value_counts()
        print(f"\n📋 Category Distribution:")
        for cat, count in category_counts.head(10).items():
            percentage = (count/len(df))*100
            print(f"   {cat}: {count} resumes ({percentage:.1f}%)")
            
        if len(category_counts) > 10:
            print(f"   ... and {len(category_counts)-10} more categories")
            
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None
    
    # 2. Load the trained model components
    try:
        print(f"\n🤖 Loading trained model components...")
        
        with open('models/resume_classifier.pkl', 'rb') as f:
            model = pickle.load(f)
        print("   ✅ Classifier loaded")
            
        with open('models/tfidf_vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
        print("   ✅ TF-IDF Vectorizer loaded")
            
        with open('models/label_encoder.pkl', 'rb') as f:
            label_encoder = pickle.load(f)
        print("   ✅ Label Encoder loaded")
        
        print(f"   📝 Model trained on {len(label_encoder.classes_)} categories:")
        for i, cat in enumerate(label_encoder.classes_[:10]):
            print(f"      {i+1}. {cat}")
        if len(label_encoder.classes_) > 10:
            print(f"      ... and {len(label_encoder.classes_)-10} more")
            
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None
    
    # 3. Prepare data for evaluation
    try:
        print(f"\n🔄 Preparing data for evaluation...")
        
        # Clean and preprocess resumes (simplified version)
        def simple_clean(text):
            import re
            import string
            text = re.sub(r'[^a-zA-Z\s]', '', str(text))
            text = text.lower().strip()
            return text
            
        df['cleaned_resume'] = df['Resume'].apply(simple_clean)
        
        # Filter to only categories that the model knows about
        df_filtered = df[df['Category'].isin(label_encoder.classes_)]
        print(f"   📊 Filtered to {len(df_filtered)} resumes with known categories")
        
        X = df_filtered['cleaned_resume'].values
        y = df_filtered['Category'].values
        
        # Transform using the trained vectorizer and encoder
        X_features = vectorizer.transform(X)
        y_encoded = label_encoder.transform(y)
        
        print(f"   ✅ Data prepared: {X_features.shape[0]} samples, {X_features.shape[1]} features")
        
    except Exception as e:
        print(f"❌ Error preparing data: {e}")
        return None
    
    # 4. Evaluate model accuracy
    try:
        print(f"\n📈 ACCURACY EVALUATION:")
        
        # Overall accuracy on full dataset
        y_pred = model.predict(X_features)
        overall_accuracy = accuracy_score(y_encoded, y_pred)
        
        print(f"   🎯 Overall Accuracy: {overall_accuracy:.1%}")
        
        # Cross-validation accuracy (more reliable)
        cv_scores = cross_val_score(model, X_features, y_encoded, cv=5, scoring='accuracy')
        cv_mean = cv_scores.mean()
        cv_std = cv_scores.std()
        
        print(f"   🔄 Cross-Validation Accuracy: {cv_mean:.1%} (±{cv_std:.1%})")
        print(f"   📊 CV Score Range: {cv_scores.min():.1%} - {cv_scores.max():.1%}")
        
        # Accuracy by category
        print(f"\n📊 ACCURACY BY CATEGORY:")
        
        # Get predictions and create classification report
        report = classification_report(y_encoded, y_pred, target_names=label_encoder.classes_, output_dict=True)
        
        category_accuracies = []
        for category in label_encoder.classes_:
            if category in report:
                precision = report[category]['precision']
                recall = report[category]['recall']
                f1_score = report[category]['f1-score']
                support = report[category]['support']
                
                category_accuracies.append({
                    'category': category,
                    'precision': precision,
                    'recall': recall,
                    'f1_score': f1_score,
                    'support': support
                })
        
        # Sort by f1-score (best overall performance metric)
        category_accuracies.sort(key=lambda x: x['f1_score'], reverse=True)
        
        print(f"   Top performing categories:")
        for i, cat_acc in enumerate(category_accuracies[:5]):
            cat = cat_acc['category']
            f1 = cat_acc['f1_score']
            support = cat_acc['support']
            print(f"   {i+1}. {cat}: {f1:.1%} F1-score ({support} samples)")
            
        print(f"\n   Lowest performing categories:")
        for i, cat_acc in enumerate(category_accuracies[-5:]):
            cat = cat_acc['category']
            f1 = cat_acc['f1_score']
            support = cat_acc['support']
            print(f"   {i+1}. {cat}: {f1:.1%} F1-score ({support} samples)")
        
    except Exception as e:
        print(f"❌ Error in accuracy evaluation: {e}")
        return None
    
    # 5. Model confidence analysis
    try:
        print(f"\n🎯 CONFIDENCE ANALYSIS:")
        
        # Get prediction probabilities
        y_proba = model.predict_proba(X_features)
        max_probabilities = np.max(y_proba, axis=1)
        
        confidence_ranges = [
            ("Very High (90-100%)", (max_probabilities >= 0.9).sum()),
            ("High (80-89%)", ((max_probabilities >= 0.8) & (max_probabilities < 0.9)).sum()),
            ("Medium (70-79%)", ((max_probabilities >= 0.7) & (max_probabilities < 0.8)).sum()),
            ("Low (60-69%)", ((max_probabilities >= 0.6) & (max_probabilities < 0.7)).sum()),
            ("Very Low (<60%)", (max_probabilities < 0.6).sum()),
        ]
        
        total_samples = len(max_probabilities)
        for range_name, count in confidence_ranges:
            percentage = (count/total_samples)*100
            print(f"   {range_name}: {count} predictions ({percentage:.1f}%)")
        
        avg_confidence = max_probabilities.mean()
        print(f"\n   📊 Average Confidence: {avg_confidence:.1%}")
        
    except Exception as e:
        print(f"❌ Error in confidence analysis: {e}")
    
    # 6. Summary and recommendations
    print(f"\n" + "="*60)
    print(f"📋 MODEL PERFORMANCE SUMMARY:")
    print(f"="*60)
    print(f"Overall Accuracy: {overall_accuracy:.1%}")
    print(f"Cross-Validation Accuracy: {cv_mean:.1%} (±{cv_std:.1%})")
    print(f"Average Confidence: {avg_confidence:.1%}")
    print(f"Training Data Size: {len(df)} resumes")
    print(f"Categories: {len(label_encoder.classes_)}")
    
    # Performance rating
    if cv_mean >= 0.9:
        rating = "🏆 EXCELLENT"
    elif cv_mean >= 0.8:
        rating = "🥇 VERY GOOD"
    elif cv_mean >= 0.7:
        rating = "🥈 GOOD"
    elif cv_mean >= 0.6:
        rating = "🥉 FAIR"
    else:
        rating = "❌ NEEDS IMPROVEMENT"
    
    print(f"Performance Rating: {rating}")
    
    return {
        'overall_accuracy': overall_accuracy,
        'cv_accuracy': cv_mean,
        'cv_std': cv_std,
        'avg_confidence': avg_confidence,
        'total_samples': len(df),
        'categories': len(label_encoder.classes_),
        'rating': rating
    }

if __name__ == "__main__":
    try:
        results = evaluate_model_accuracy()
        if results:
            print(f"\n✅ Model evaluation completed successfully!")
        else:
            print(f"\n❌ Model evaluation failed!")
    except Exception as e:
        print(f"❌ Error running evaluation: {e}")
        import traceback
        traceback.print_exc()
