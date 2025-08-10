@echo off
echo ========================================
echo   RENDER DEPLOYMENT HELPER SCRIPT
echo ========================================
echo.

echo Step 1: Checking if Git is installed...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git is not installed!
    echo Please install Git from: https://git-scm.com/download/win
    echo Then run this script again.
    pause
    exit /b 1
)
echo ✅ Git is installed

echo.
echo Step 2: Initializing Git repository...
git init
if %errorlevel% neq 0 (
    echo Repository already initialized
)

echo.
echo Step 3: Adding all files...
git add .

echo.
echo Step 4: Creating commit...
git commit -m "Resume Screening AI - Ready for Render deployment"

echo.
echo Step 5: Setting up remote repository...
git remote remove origin >nul 2>&1
git remote add origin https://github.com/Anandkumar04/Resume-screening-fullStack.git

echo.
echo Step 6: Setting main branch...
git branch -M main

echo.
echo Step 7: Pushing to GitHub...
echo Note: You may need to enter your GitHub credentials
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ SUCCESS! Your code is now on GitHub!
    echo.
    echo 🎯 NEXT STEPS:
    echo 1. Go to https://render.com
    echo 2. Sign up with your GitHub account
    echo 3. Create new Web Service
    echo 4. Select your Resume-screening-fullStack repository
    echo 5. Use these settings:
    echo    - Runtime: Python 3
    echo    - Build Command: pip install -r requirements.txt
    echo    - Start Command: gunicorn wsgi:app --bind 0.0.0.0:$PORT
    echo    - Root Directory: resume_screening_api
    echo.
    echo 🚀 Your app will be live at: https://your-app-name.onrender.com
    echo.
) else (
    echo ❌ Push failed. Please check your GitHub credentials and try again.
)

echo.
pause
