# 🎨 RENDER DEPLOYMENT GUIDE

## Why Choose Render:
- ✅ **Free tier** with no sleep time
- ✅ **Automatic HTTPS**
- ✅ **GitHub integration**
- ✅ **Modern platform**
- ✅ **Better performance than Heroku free tier**

## Step 1: Prepare Repository
1. Push your code to GitHub:
   ```bash
   git remote add origin https://github.com/Anandkumar04/Resume-Screening.git
   git branch -M main
   git push -u origin main
   ```

## Step 2: Deploy on Render
1. Go to https://render.com
2. Sign up with GitHub
3. Click "New" → "Web Service"
4. Connect your GitHub repository
5. Configure deployment:

**Build Settings:**
- **Build Command**: `cd resume_screening_api && pip install -r requirements.txt`
- **Start Command**: `cd resume_screening_api && gunicorn wsgi:app --bind 0.0.0.0:$PORT`

**Environment Variables:**
```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
MAX_CONTENT_LENGTH=16777216
```

## Step 3: Deploy
- Click "Create Web Service"
- Wait 5-10 minutes for deployment
- Your app will be live at: `https://your-app-name.onrender.com`

## Cost:
- **Free Tier**: Unlimited apps (some limitations)
- **Paid Tier**: $7/month per service
