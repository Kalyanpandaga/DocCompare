from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from document_processor import DocumentProcessor
from similarity_calculator import SimilarityCalculator

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize processors
document_processor = DocumentProcessor()
similarity_calculator = SimilarityCalculator()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process the document
        processed_doc = document_processor.process_document(filepath)
        
        return jsonify({
            'message': 'File uploaded successfully',
            'filename': filename,
            'processed_doc': processed_doc
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/compare', methods=['POST'])
def compare_documents():
    data = request.json
    if not data or 'doc1' not in data or 'doc2' not in data:
        return jsonify({'error': 'Missing document data'}), 400
    
    try:
        similarity_score = similarity_calculator.calculate_similarity(
            data['doc1'],
            data['doc2']
        )
        
        return jsonify({
            'similarity_score': similarity_score
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000) 