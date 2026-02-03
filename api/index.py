import sys
import os

# Add the project root to the path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

# Export the FastAPI app for Vercel
# Vercel's Python runtime will handle ASGI apps directly
