# ☁️ AWS DEPLOYMENT GUIDE

## Option A: AWS Elastic Beanstalk (Easier)

### Step 1: Prepare Application
Create `application.py` (AWS expects this name):
```python
from wsgi import app as application

if __name__ == "__main__":
    application.run()
```

### Step 2: Create ZIP Package
```bash
# Create deployment package
zip -r resume-screening-ai.zip . -x "*.git*" "*.env*" "__pycache__/*"
```

### Step 3: Deploy on Elastic Beanstalk
1. Go to AWS Console → Elastic Beanstalk
2. Create new application
3. Choose "Python" platform
4. Upload your ZIP file
5. Configure environment variables

## Option B: AWS EC2 (Full Control)

### Step 1: Launch EC2 Instance
1. Launch Ubuntu 22.04 instance
2. Choose t2.micro (free tier)
3. Configure security group (ports 80, 443, 22)

### Step 2: Setup Server
```bash
# SSH into your instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3-pip python3-venv nginx git -y

# Clone your repository
git clone https://github.com/Anandkumar04/Resume-Screening.git
cd Resume-Screening/resume_screening_api

# Create virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Install and configure gunicorn
pip install gunicorn
```

### Step 3: Configure Nginx
```bash
sudo nano /etc/nginx/sites-available/resume-ai
```

Add configuration:
```nginx
server {
    listen 80;
    server_name your-domain-or-ip;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    client_max_body_size 20M;
}
```

### Step 4: Start Services
```bash
# Enable Nginx site
sudo ln -s /etc/nginx/sites-available/resume-ai /etc/nginx/sites-enabled
sudo systemctl restart nginx

# Start Gunicorn
gunicorn wsgi:app --bind 127.0.0.1:8000 --workers 3 --daemon

# Make it permanent with systemd
sudo nano /etc/systemd/system/resume-ai.service
```

## Cost:
- **Free Tier**: 750 hours/month EC2 micro instance
- **Paid**: $10-50/month depending on usage
