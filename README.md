# AI Resume Screening System 

## 🎯 Project Overview

Resume Screening AI is a full-stack web application that leverages machine learning to automatically classify resumes into job categories. It processes multiple file formats (PDF, DOC, TXT) and provides real-time classification with confidence scores, helping organizations streamline their hiring workflow.

---

## 💡 Technical Architecture

### Backend (Python/Flask)
- **Framework:** Flask web application with RESTful API
- **ML Pipeline:** scikit-learn (K-Nearest Neighbors classifier)
- **Text Processing:** TF-IDF vectorization for feature extraction
- **File Handling:** PyPDF2 and pdfplumber for robust PDF text extraction
- **Data Processing:** NLTK for text cleaning and preprocessing

### Frontend
- **UI:** Responsive design powered by Bootstrap 5
- **JavaScript:** Asynchronous form submission via Fetch API
- **UX:** Real-time feedback, loading states, and error handling for seamless user experience

### Data Flow
1. **User uploads resume** (PDF/DOC/TXT) or pastes text
2. **Backend extracts and cleans text content**
3. **ML model processes text** using trained TF-IDF vectors
4. **Returns predicted job category with confidence score**

---

## 🔧 Technical Challenges & Solutions

**1. PDF Text Extraction**
- **Challenge:** PDFs could not be read as plain text
- **Solution:** Dual PDF processing (PyPDF2 + pdfplumber fallback)
- **Lesson:** Robust file format handling and error management

**2. Python 3.13 Compatibility**
- **Challenge:** Package compatibility issues
- **Solution:** Flexible version constraints in `requirements.txt`
- **Lesson:** Dependency management is key for maintainability

**3. Frontend-Backend Integration**
- **Challenge:** Form submission not triggering
- **Solution:** Implemented event listeners with DOMContentLoaded
- **Lesson:** Console log debugging essential for JavaScript

---

## 📊 Machine Learning Implementation

- **Data Preprocessing:** Text cleaning, tokenization
- **Model Training:**
  - **Algorithm:** K-Nearest Neighbors (KNN)
  - **Features:** TF-IDF vectors (bag-of-words)
  - **Training Data:** Resume dataset with job category labels
  - **Evaluation:** Cross-validation for model performance

**Why KNN + TF-IDF?**
- Simple, interpretable, effective for text classification
- TF-IDF highlights important words, reduces noise
- Easy scalability with new data

---

## 🎨 Full-Stack Skills Demonstrated

| Frontend           | Backend        | ML/Data         | DevOps           |
|--------------------|---------------|-----------------|------------------|
| HTML5/CSS3         | Python/Flask  | scikit-learn    | Git              |
| JavaScript (ES6+)  | RESTful APIs  | NLTK            | Debug/Testing    |
| Bootstrap 5        | File handling | Data preprocessing | Environment setup |
| Responsive design  | Error handling| Model evaluation| Dependency management |

---

## 🚀 Key Accomplishments

- **End-to-End Development:** Complete ML pipeline and web integration
- **Multi-Format Support:** PDF, DOC, DOCX, and text files
- **Real-time Processing:** Instant classification and feedback
- **Production-Ready:** Robust error handling, validation, and UX
- **Scalable Architecture:** Easily extendable to new categories or higher accuracy

---

## 💼 Business Impact

- **Time Saving:** Automates manual resume screening
- **Consistency:** Removes human bias from initial screening
- **Scalability:** Processes hundreds of resumes quickly
- **Cost Effective:** Reduces HR workload for large-scale hiring

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+ (recommended)
- Node.js (for frontend development, optional)
- [pip](https://pip.pypa.io/en/stable/) for Python dependencies

### Installation

```bash
git clone https://github.com/Anandkumar04/resume-screening-ai.git
cd resume-screening-ai
pip install -r requirements.txt
```

### Running the Application

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📝 File Formats Supported

- PDF, DOC, DOCX, TXT

## 📈 Output

- Predicted job category
- Confidence score for classification

---

## 🤝 Contributing

Contributions are welcome! Please open issues or pull requests for improvements, new features, or bug fixes.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👀 Demo

![Demo Screenshot](demo/demo_screenshot.png)

---

## 📬 Contact

For questions or feedback, open an issue or reach out to [Anandkumar04](https://github.com/Anandkumar04).
