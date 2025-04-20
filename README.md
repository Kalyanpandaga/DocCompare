# Document Similarity Detection System

A system for detecting duplicate or highly similar text documents using advanced similarity algorithms.

## Project Structure

```
documents_cleaner/
├── backend/           # Python backend for document processing
├── frontend/          # React frontend for document upload and comparison
├── docs/             # Documentation and system design
└── tests/            # Test files
```

## Features

- Document upload and processing
- Similarity score calculation between documents
- Visual representation of document similarity
- Support for multiple document formats

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows (PowerShell): `.\venv\Scripts\activate`
   - Windows (Command Prompt): `venv\Scripts\activate.bat`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the server: `python app.py`

### Frontend Setup

1. Navigate to the frontend directory
2. Install dependencies: `npm install`
3. Start the development server: `npm start`

## System Design

See `docs/system_design.md` for detailed system architecture and design decisions.

## Testing

Run tests using: `python -m pytest tests/`

## License

MIT
