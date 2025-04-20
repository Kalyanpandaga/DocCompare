from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SimilarityCalculator:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
    
    def calculate_similarity(self, doc1, doc2):
        """
        Calculate similarity score between two documents using TF-IDF and cosine similarity.
        
        Args:
            doc1 (str): First document text
            doc2 (str): Second document text
            
        Returns:
            float: Similarity score between 0 and 1
        """
        try:
            # Create TF-IDF vectors
            tfidf_matrix = self.vectorizer.fit_transform([doc1, doc2])
            
            # Calculate cosine similarity
            similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
            
            # Return the similarity score
            return float(similarity_matrix[0][0])
            
        except Exception as e:
            raise Exception(f"Error calculating similarity: {str(e)}")
    
    def batch_similarity(self, documents):
        """
        Calculate similarity scores for multiple documents.
        
        Args:
            documents (list): List of document texts
            
        Returns:
            numpy.ndarray: Matrix of similarity scores
        """
        try:
            # Create TF-IDF vectors for all documents
            tfidf_matrix = self.vectorizer.fit_transform(documents)
            
            # Calculate pairwise cosine similarity
            similarity_matrix = cosine_similarity(tfidf_matrix)
            
            return similarity_matrix
            
        except Exception as e:
            raise Exception(f"Error calculating batch similarity: {str(e)}") 