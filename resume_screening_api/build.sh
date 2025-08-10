#!/bin/bash

# Render.com runtime configuration
# This script runs during the build process to ensure all dependencies are properly installed

echo "🔧 RENDER BUILD: Installing PDF processing dependencies..."

# Force install PDF processing libraries
echo "📥 Installing PyPDF2..."
pip install PyPDF2==3.0.1 --force-reinstall

echo "📥 Installing pdfplumber..."
pip install pdfplumber==0.9.0 --force-reinstall

echo "📥 Installing python-docx..."
pip install python-docx==0.8.11 --force-reinstall

echo "📥 Installing additional dependencies..."
pip install cryptography==41.0.7
pip install typing-extensions==4.8.0

echo "✅ PDF processing dependencies installed successfully!"

# Verify installations
echo "🔍 Verifying installations..."
python -c "import PyPDF2; print(f'PyPDF2 version: {PyPDF2.__version__}')"
python -c "import pdfplumber; print(f'pdfplumber version: {pdfplumber.__version__}')"
python -c "from docx import Document; print('python-docx imported successfully')"

echo "🎉 All PDF processing libraries are ready!"
