# 🌊 DIGITALOCEAN DEPLOYMENT GUIDE

## Why Choose DigitalOcean:
- ✅ **Professional hosting**
- ✅ **$200 free credit** for new users
- ✅ **Predictable pricing**
- ✅ **Great performance**

## Step 1: Create App
1. Go to https://cloud.digitalocean.com/apps
2. Click "Create App"
3. Connect your GitHub repository
4. Select branch: `main`

## Step 2: Configure App
**App Spec Configuration:**
```yaml
name: resume-screening-ai
services:
- name: web
  source_dir: /resume_screening_api
  github:
    repo: Anandkumar04/Resume-Screening
    branch: main
  run_command: gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 2
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs
  http_port: 8080
  envs:
  - key: FLASK_ENV
    value: production
  - key: SECRET_KEY
    value: your-secret-key-here
```

## Step 3: Deploy
- Review configuration
- Click "Create Resources"
- Wait for deployment (5-10 minutes)

## Cost:
- **Basic Plan**: $5/month
- **Professional**: $12/month
