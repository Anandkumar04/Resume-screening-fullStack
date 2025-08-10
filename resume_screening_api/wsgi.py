"""
WSGI entry point for production deployment
"""
import os
import sys

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Import the main Flask app
from app import app

# For Gunicorn and other WSGI servers
if __name__ == "__main__":
    # This runs when called directly (not through WSGI server)
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
