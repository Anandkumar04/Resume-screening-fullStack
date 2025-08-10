# 🚀 HEROKU DEPLOYMENT GUIDE

## Prerequisites
1. Create account at https://heroku.com
2. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
3. Install Git (if not already installed)

## Step 1: Prepare Your Project
```bash
cd "C:\Users\91934\OneDrive\Documents\webdev\Full-stack-projects\Resume-Screening"

# Initialize git repository (if not already done)
git init
git add .
git commit -m "Initial commit - Resume Screening AI"
```

## Step 2: Login to Heroku
```bash
heroku login
```

## Step 3: Create Heroku App
```bash
# Create new app (choose unique name)
heroku create your-resume-ai-app

# Or let Heroku generate random name
heroku create
```

## Step 4: Configure Environment Variables
```bash
# Set production environment
heroku config:set FLASK_ENV=production

# Set secret key (generate random string)
heroku config:set SECRET_KEY=your-super-secret-key-here-change-this

# Set max file size (16MB)
heroku config:set MAX_CONTENT_LENGTH=16777216

# Verify settings
heroku config
```

## Step 5: Deploy to Heroku
```bash
# Deploy your app
git push heroku main

# If you're on different branch
git push heroku your-branch-name:main
```

## Step 6: Open Your App
```bash
# Open in browser
heroku open

# Or check logs if there are issues
heroku logs --tail
```

## Your App URLs:
- **Dashboard**: https://dashboard.heroku.com/apps/your-app-name
- **Live App**: https://your-app-name.herokuapp.com
- **Logs**: `heroku logs --tail`

## Troubleshooting:
```bash
# Check app status
heroku ps

# Restart app
heroku restart

# Check logs
heroku logs --tail

# Scale dynos
heroku ps:scale web=1
```

## Cost: 
- **Free Tier**: 0-1000 dyno hours/month (enough for portfolio)
- **Paid Tier**: $7/month (always-on, custom domain)
