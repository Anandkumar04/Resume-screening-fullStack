from flask import Flask, render_template, request, jsonify
import pickle
import os
import re
from werkzeug.utils import secure_filename

# Import PDF and document processing libraries with better error handling
PDF_SUPPORT = False
PDFPLUMBER_SUPPORT = False
DOC_SUPPORT = False

# Try importing PyPDF2
try:
    import PyPDF2
    PDF_SUPPORT = True
    print("✅ PyPDF2 imported successfully")
    print(f"   PyPDF2 version: {PyPDF2.__version__}")
except ImportError as e:
    print(f"❌ PyPDF2 import failed: {e}")
    print("   Attempting to install PyPDF2...")
    try:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2==3.0.1"])
        import PyPDF2
        PDF_SUPPORT = True
        print("✅ PyPDF2 installed and imported successfully")
    except Exception as install_error:
        print(f"❌ Failed to install PyPDF2: {install_error}")

# Try importing pdfplumber
try:
    import pdfplumber
    PDFPLUMBER_SUPPORT = True  
    print("✅ pdfplumber imported successfully")
    print(f"   pdfplumber version: {pdfplumber.__version__}")
except ImportError as e:
    print(f"❌ pdfplumber import failed: {e}")
    print("   Attempting to install pdfplumber...")
    try:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pdfplumber==0.9.0"])
        import pdfplumber
        PDFPLUMBER_SUPPORT = True
        print("✅ pdfplumber installed and imported successfully")
    except Exception as install_error:
        print(f"❌ Failed to install pdfplumber: {install_error}")

# Try importing python-docx
try:
    from docx import Document
    DOC_SUPPORT = True
    print("✅ python-docx imported successfully")
except ImportError as e:
    print(f"❌ python-docx import failed: {e}")
    print("   Attempting to install python-docx...")
    try:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx==0.8.11"])
        from docx import Document
        DOC_SUPPORT = True
        print("✅ python-docx installed and imported successfully")
    except Exception as install_error:
        print(f"❌ Failed to install python-docx: {install_error}")

# Check PDF support status
if PDF_SUPPORT or PDFPLUMBER_SUPPORT:
    print("✅ PDF processing libraries available")
    if PDF_SUPPORT:
        print("   - PyPDF2 ready")
    if PDFPLUMBER_SUPPORT:
        print("   - pdfplumber ready")
else:
    print("⚠️  WARNING: No PDF processing support available!")

# Download NLTK data if not already present
try:
    import nltk
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    print("Downloading NLTK data...")
    nltk.download('punkt')
    nltk.download('stopwords')

app = Flask(__name__)

# Production configuration
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = int(os.getenv('MAX_CONTENT_LENGTH', '16777216'))  # 16MB default
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Security settings for production
if os.getenv('FLASK_ENV') == 'production':
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def extract_text_from_file(file_path, file_extension):
    """
    Extract text from different file types
    
    Args:
        file_path (str): Path to the file
        file_extension (str): File extension (e.g., '.pdf', '.txt', '.docx')
    
    Returns:
        str: Extracted text content
    """
    text = ""
    
    try:
        if file_extension.lower() == '.pdf':
            if not PDF_SUPPORT and not PDFPLUMBER_SUPPORT:
                raise Exception("PDF support not available. Please install PyPDF2 or pdfplumber.")
            
            # Try PyPDF2 first, then pdfplumber as fallback
            pdf_extracted = False
            
            if PDF_SUPPORT:
                try:
                    print("🔄 Attempting PDF extraction with PyPDF2...")
                    with open(file_path, 'rb') as file:
                        pdf_reader = PyPDF2.PdfReader(file)
                        for page_num in range(len(pdf_reader.pages)):
                            page = pdf_reader.pages[page_num]
                            page_text = page.extract_text()
                            if page_text.strip():  # Only add non-empty text
                                text += page_text + "\n"
                    
                    if text.strip():  # If we got some text
                        pdf_extracted = True
                        print("✅ PyPDF2 extraction successful")
                    else:
                        print("⚠️  PyPDF2 extracted empty text, trying pdfplumber...")
                        
                except Exception as pypdf_error:
                    print(f"⚠️  PyPDF2 failed: {pypdf_error}")
            
            # Try pdfplumber if PyPDF2 failed or wasn't available
            if not pdf_extracted and PDFPLUMBER_SUPPORT:
                try:
                    print("🔄 Attempting PDF extraction with pdfplumber...")
                    import pdfplumber
                    with pdfplumber.open(file_path) as pdf:
                        for page in pdf.pages:
                            page_text = page.extract_text()
                            if page_text:
                                text += page_text + "\n"
                    print("✅ pdfplumber extraction successful")
                    pdf_extracted = True
                except Exception as plumber_error:
                    print(f"⚠️  pdfplumber failed: {plumber_error}")
            
            if not pdf_extracted:
                raise Exception("Failed to extract text from PDF with both PyPDF2 and pdfplumber")
                        
        elif file_extension.lower() in ['.docx', '.doc']:
            if not DOC_SUPPORT:
                raise Exception("Word document support not available. Please install python-docx.")
            
            # Use python-docx to extract text from Word documents
            try:
                doc = Document(file_path)
                for paragraph in doc.paragraphs:
                    text += paragraph.text + "\n"
            except Exception as e:
                raise Exception(f"Error reading Word document: {str(e)}")
                        
        elif file_extension.lower() in ['.txt', '.text']:
            # Handle plain text files
            encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        text = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            
        elif file_extension.lower() == '.docx':
            # For future implementation - would need python-docx
            raise Exception("DOCX files not yet supported. Please convert to PDF or text format.")
            
        else:
            # Default: try to read as text file
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
            except UnicodeDecodeError:
                with open(file_path, 'r', encoding='latin-1') as f:
                    text = f.read()
    
    except Exception as e:
        raise Exception(f"Error extracting text from {file_extension} file: {str(e)}")
    
    if not text.strip():
        raise Exception(f"No text could be extracted from the {file_extension} file")
    
    return text.strip()

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

def load_model():
    """Load the trained model, vectorizer, and label encoder"""
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
    """Predict the category of a resume"""
    import numpy as np
    
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

# Load the trained model and vectorizer on startup
try:
    model, vectorizer, label_encoder = load_model()
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model, vectorizer, label_encoder = None, None, None

@app.route('/')
def index():
    """Main page with resume upload form"""
    return render_template('index.html')

@app.route('/test-page')
def test_page():
    """Test page for debugging"""
    return render_template('test.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    """Test endpoint to debug issues"""
    if request.method == 'GET':
        return jsonify({'message': 'Test endpoint is working', 'method': 'GET'})
    else:
        return jsonify({
            'message': 'Test endpoint is working', 
            'method': 'POST',
            'form_data': dict(request.form),
            'files': list(request.files.keys())
        })

@app.route('/predict', methods=['POST'])
def predict():
    """API endpoint for resume classification"""
    print(f"=== PREDICT REQUEST START ===")
    print(f"Request method: {request.method}")
    print(f"Content type: {request.content_type}")
    print(f"Form keys: {list(request.form.keys())}")
    print(f"Files keys: {list(request.files.keys())}")
    
    try:
        resume_text = ""
        
        # Handle form data submission
        if request.form.get('resume_text'):
            resume_text = request.form.get('resume_text').strip()
            print(f"Using text input, length: {len(resume_text)}")
        elif 'resume_file' in request.files and request.files['resume_file'].filename:
            # File upload
            file = request.files['resume_file']
            print(f"Processing file: {file.filename}")
            if file.filename == '':
                return jsonify({'error': 'No file selected'}), 400
            
            # Save file temporarily
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Extract text based on file type
            try:
                file_extension = os.path.splitext(filename)[1].lower()
                print(f"File extension: {file_extension}")
                
                # Check if file type is supported
                allowed_extensions = ['.pdf', '.txt', '.docx', '.doc']
                if file_extension not in allowed_extensions:
                    os.remove(filepath)
                    return jsonify({
                        'error': f'Unsupported file type: {file_extension}. Supported types: PDF, TXT, DOC, DOCX'
                    }), 400
                
                # Extract text from file
                resume_text = extract_text_from_file(filepath, file_extension)
                os.remove(filepath)  # Clean up
                print(f"Text extracted successfully, length: {len(resume_text)}")
                
            except Exception as e:
                print(f"Error extracting text from file: {e}")
                if os.path.exists(filepath):
                    os.remove(filepath)  # Clean up
                return jsonify({'error': f'Error reading file: {str(e)}'}), 400
        else:
            print("No resume text or file found in request")
            return jsonify({'error': 'No resume text or file provided. Please enter text or upload a file.'}), 400

        if not resume_text.strip():
            print("Resume text is empty")
            return jsonify({'error': 'Resume text is empty'}), 400

        if not model or not vectorizer or not label_encoder:
            print("Model components not loaded")
            return jsonify({'error': 'Model not loaded. Please train the model first.'}), 500

        print("Starting text cleaning...")
        # Clean the resume text
        cleaned_text = clean_resume(resume_text)
        print(f"Text cleaned, length: {len(cleaned_text)}")
        
        if not cleaned_text.strip():
            print("Cleaned text is empty")
            return jsonify({'error': 'Resume text is empty after cleaning'}), 400
        
        print("Making prediction...")
        # Make prediction
        category, probability = predict_category(cleaned_text, model, vectorizer, label_encoder)
        print(f"Prediction successful: {category} ({probability:.2%})")
        
        result = {
            'category': category,
            'confidence': f"{probability:.2%}",
            'cleaned_text_preview': cleaned_text[:200] + "..." if len(cleaned_text) > 200 else cleaned_text
        }
        print(f"Returning result: {result}")
        return jsonify(result)

    except Exception as e:
        print(f"Exception in predict endpoint: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/api/categories')
def get_categories():
    """Get all available categories"""
    try:
        # Read the dataset to get categories using CSV module
        import csv
        categories = set()
        with open('../resume_dataset.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if 'Category' in row:
                    categories.add(row['Category'])
        return jsonify({'categories': list(categories)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/train', methods=['POST'])
def train_model():
    """API endpoint to retrain the model"""
    try:
        import subprocess
        result = subprocess.run(['python', 'models/train_model.py'], 
                              capture_output=True, text=True, cwd='.')
        if result.returncode == 0:
            # Reload the model
            global model, vectorizer, label_encoder
            model, vectorizer, label_encoder = load_model()
            return jsonify({
                'message': 'Model trained successfully!',
                'output': result.stdout
            })
        else:
            return jsonify({'error': f'Training failed: {result.stderr}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/about')
def about():
    """About page with project information"""
    return render_template('about.html')

if __name__ == '__main__':
    # Development mode
    app.run(debug=True, host='127.0.0.1', port=5000)
