import sys
import os

# Add the project directory to sys.path (global import path)
project_path = os.path.abspath(os.path.dirname(__file__))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Import the Flask app as the WSGI application
from app import app as application

#python run_global.py