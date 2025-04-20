import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import os
import chardet

class DocumentProcessor:
    def __init__(self):
        # Download required NLTK data
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
    
    def process_document(self, filepath):
        """Process a document and return its cleaned text representation."""
        try:
            # Try to detect encoding first
            with open(filepath, 'rb') as file:
                raw_data = file.read()
                result = chardet.detect(raw_data)
                encoding = result['encoding']
            
            # List of encodings to try
            encodings_to_try = [
                encoding,  # Try detected encoding first
                'utf-8',
                'latin-1',
                'cp1252',
                'iso-8859-1',
                'ascii'
            ]
            
            text = None
            for enc in encodings_to_try:
                try:
                    with open(filepath, 'r', encoding=enc) as file:
                        text = file.read()
                    break  # If successful, break the loop
                except UnicodeDecodeError:
                    continue  # Try next encoding
            
            if text is None:
                # If all encodings fail, try reading as binary and decode with errors='replace'
                with open(filepath, 'rb') as file:
                    text = file.read().decode('utf-8', errors='replace')
            
            # Clean and process the text
            processed_text = self._preprocess_text(text)
            
            return processed_text
            
        except Exception as e:
            raise Exception(f"Error processing document: {str(e)}")
    
    def _preprocess_text(self, text):
        """Preprocess the text by cleaning, tokenizing, and normalizing."""
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords and stem
        processed_tokens = [
            self.stemmer.stem(token)
            for token in tokens
            if token not in self.stop_words and len(token) > 1
        ]
        
        return ' '.join(processed_tokens)
    
    def _extract_text_from_pdf(self, filepath):
        """Extract text from PDF files."""
        # This would be implemented using a PDF processing library
        # For now, we'll just return an empty string
        return ""
    
    def _extract_text_from_docx(self, filepath):
        """Extract text from DOCX files."""
        # This would be implemented using a DOCX processing library
        # For now, we'll just return an empty string
        return "" 