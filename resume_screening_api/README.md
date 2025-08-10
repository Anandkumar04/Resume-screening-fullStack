# Resume Screening API

A Flask web application that uses machine learning to automatically categorize resumes based on job roles.

## 🚀 Features

- **AI-Powered Classification**: Uses K-Nearest Neighbors with TF-IDF vectorization
- **Multiple Input Methods**: Upload files or paste resume text directly
- **Real-time Analysis**: Instant resume categorization with confidence scores
- **Responsive Web Interface**: Modern, mobile-friendly design
- **RESTful API**: Easy integration with other systems
- **Secure Processing**: Resume data is processed but not permanently stored

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## 🛠️ Installation

1. **Navigate to the API directory**:
   ```bash
   cd resume_screening_api
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK data** (if not already done):
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

4. **Set up and train the model**:
   ```bash
   python setup.py
   ```

## 🎯 Usage

### Starting the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Web Interface

1. **Home Page** (`/`): Upload resume files or paste text for classification
2. **About Page** (`/about`): Learn more about the project and technology

### API Endpoints

#### Classify Resume
- **URL**: `/predict`
- **Method**: `POST`
- **Content-Type**: `multipart/form-data` or `application/x-www-form-urlencoded`
- **Parameters**:
  - `resume_text`: Resume text (string)
  - `resume_file`: Resume file upload

**Example Response**:
```json
{
  "category": "Data Science",
  "confidence": "87.45%",
  "cleaned_text_preview": "Skills Programming Languages Python pandas numpy..."
}
```

#### Get Categories
- **URL**: `/api/categories`
- **Method**: `GET`

**Example Response**:
```json
{
  "categories": ["Data Science", "Web Development", "Mobile Development", ...]
}
```

#### Retrain Model
- **URL**: `/train`
- **Method**: `POST`

**Example Response**:
```json
{
  "message": "Model trained successfully!",
  "accuracy": "92.15%"
}
```

## 📁 Project Structure

```
resume_screening_api/
├── app.py                  # Main Flask application
├── setup.py               # Setup and model training script
├── requirements.txt        # Python dependencies
├── models/
│   ├── train_model.py     # Model training script
│   ├── resume_classifier.pkl    # Trained model (generated)
│   ├── tfidf_vectorizer.pkl     # TF-IDF vectorizer (generated)
│   └── label_encoder.pkl        # Label encoder (generated)
├── preprocessing/
│   └── text_cleaner.py    # Text preprocessing functions
├── utils/
│   └── model_utils.py     # Model utility functions
├── templates/
│   ├── index.html         # Main page template
│   └── about.html         # About page template
├── static/                # Static files (CSS, JS, images)
└── uploads/               # Temporary file uploads
```

## 🧠 Machine Learning Pipeline

1. **Data Loading**: Load resume dataset from CSV
2. **Text Cleaning**: Remove URLs, mentions, punctuation, extra whitespace
3. **Feature Extraction**: TF-IDF vectorization with 1500 max features
4. **Model Training**: K-Nearest Neighbors with OneVsRest classification
5. **Model Persistence**: Save trained model, vectorizer, and label encoder

## 🎨 Technology Stack

- **Backend**: Flask, Python
- **Machine Learning**: Scikit-learn, NLTK
- **Data Processing**: Pandas, NumPy
- **Frontend**: Bootstrap 5, JavaScript, HTML5/CSS3
- **Model Persistence**: Pickle

## 🔧 Configuration

### Environment Variables (Optional)
- `FLASK_ENV`: Set to `development` for debug mode
- `FLASK_PORT`: Custom port (default: 5000)

### Model Parameters
You can modify the model parameters in `models/train_model.py`:
- `max_features`: TF-IDF max features (default: 1500)
- `n_neighbors`: KNN neighbors (default: 5)
- `test_size`: Train/test split ratio (default: 0.2)

## 📊 Supported Resume Categories

The model can classify resumes into various categories including:
- Data Science
- Web Development 
- Mobile Development
- DevOps Engineering
- UI/UX Design
- And more...

## 🚨 Troubleshooting

### Common Issues

1. **Model files not found**:
   ```bash
   python setup.py
   ```

2. **NLTK data missing**:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

3. **Port already in use**:
   ```bash
   python app.py --port 5001
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📜 License

This project is licensed under the MIT License.

## 🙋‍♀️ Support

For questions or issues:
1. Check the troubleshooting section
2. Review the error logs
3. Open an issue in the repository

---

**Note**: Make sure the `resume_dataset.csv` file is in the parent directory before running the setup script.
