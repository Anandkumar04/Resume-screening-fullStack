import pandas as pd
import joblib

# Check what categories are in the dataset
print("=== CHECKING DATASET CATEGORIES ===")
try:
    df = pd.read_csv('../resume_dataset.csv')
    categories = df['Category'].value_counts()
    print(f"\nFound {len(categories)} categories in dataset:")
    for cat, count in categories.items():
        print(f"- {cat}: {count} resumes")
except Exception as e:
    print(f"Error reading dataset: {e}")

print("\n" + "="*50)

# Check what categories the trained model knows
print("=== CHECKING TRAINED MODEL CATEGORIES ===")
try:
    label_encoder = joblib.load('models/label_encoder.pkl')
    print(f"\nModel was trained on {len(label_encoder.classes_)} categories:")
    for i, cat in enumerate(label_encoder.classes_):
        print(f"{i+1}. {cat}")
except Exception as e:
    print(f"Error loading model: {e}")
