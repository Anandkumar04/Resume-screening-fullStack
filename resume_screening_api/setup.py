"""
Setup script for Resume Screening API
This script trains the model and prepares the application for use.
"""

import os
import sys

def setup_environment():
    """Set up the environment and train the model"""
    print("=" * 60)
    print("Resume Screening API Setup")
    print("=" * 60)
    
    # Check if we're in the correct directory
    if not os.path.exists('app.py'):
        print("❌ Error: Please run this script from the resume_screening_api directory")
        return False
    
    print("✅ Setting up environment...")
    
    # Create uploads directory
    os.makedirs('uploads', exist_ok=True)
    print("✅ Created uploads directory")
    
    # Check if dataset exists
    dataset_path = '../resume_dataset.csv'
    if not os.path.exists(dataset_path):
        print(f"❌ Error: Dataset not found at {dataset_path}")
        print("Please ensure resume_dataset.csv is in the parent directory")
        return False
    
    print("✅ Dataset found")
    
    # Train the model
    print("\n📚 Training the machine learning model...")
    print("This may take a few minutes...")
    
    try:
        from models.train_model import train_and_save_model
        accuracy = train_and_save_model()
        print(f"✅ Model trained successfully with {accuracy:.2%} accuracy")
    except Exception as e:
        print(f"❌ Error training model: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 Setup completed successfully!")
    print("=" * 60)
    print("\nTo start the Flask application:")
    print("1. Install requirements: pip install -r requirements.txt")
    print("2. Run the app: python app.py")
    print("3. Open your browser to: http://localhost:5000")
    print("\nNote: Make sure you have all required packages installed!")
    
    return True

if __name__ == "__main__":
    success = setup_environment()
    if not success:
        sys.exit(1)
