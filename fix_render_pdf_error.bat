@echo off
echo =======================================
echo   FIXING RENDER PDF PROCESSING ERROR
echo =======================================
echo.

echo Your analysis is CORRECT! 
echo The issue: PyPDF2 wasn't properly installed on Render
echo.

echo Step 1: Checking current directory...
cd /d "c:\Users\91934\OneDrive\Documents\webdev\Full-stack-projects\Resume-Screening"
echo Current directory: %CD%

echo.
echo Step 2: Adding updated requirements.txt...
git add resume_screening_api/requirements.txt
git add resume_screening_api/requirements-render.txt

echo.
echo Step 3: Committing the fix...
git commit -m "Fix PDF processing: Added PyPDF2 and exact versions to requirements.txt"

echo.
echo Step 4: Pushing to GitHub...
git push origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ SUCCESS! Requirements.txt updated and pushed to GitHub!
    echo.
    echo 🔄 NEXT STEPS:
    echo 1. Go to your Render dashboard: https://dashboard.render.com
    echo 2. Find your Resume Screening AI service
    echo 3. Click "Manual Deploy" or wait for auto-deploy
    echo 4. Monitor the build logs to see PyPDF2 being installed
    echo 5. Test PDF upload once deployment completes
    echo.
    echo 📋 What was fixed:
    echo • Added exact versions to requirements.txt
    echo • Included PyPDF2==3.0.1
    echo • Added pdfplumber==0.9.0  
    echo • Added python-docx==0.8.11
    echo.
    echo 🎯 Your PDF processing should now work on Render!
) else (
    echo ❌ Push failed. Please check your Git setup and try again.
)

echo.
pause
