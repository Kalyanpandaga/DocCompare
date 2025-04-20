import os
import sys

def ensure_directories():
    # Get the absolute path of the backend directory
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create uploads directory if it doesn't exist
    uploads_dir = os.path.join(backend_dir, 'uploads')
    os.makedirs(uploads_dir, exist_ok=True)
    
    print(f"Ensured directory exists: {uploads_dir}")

if __name__ == '__main__':
    ensure_directories() 