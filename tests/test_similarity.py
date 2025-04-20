import pytest
from backend.similarity_calculator import SimilarityCalculator

def test_similarity_calculation():
    calculator = SimilarityCalculator()
    
    # Test identical documents
    doc1 = "This is a test document for similarity calculation"
    doc2 = "This is a test document for similarity calculation"
    score = calculator.calculate_similarity(doc1, doc2)
    assert score == 1.0, "Identical documents should have similarity score of 1.0"
    
    # Test completely different documents
    doc1 = "This is the first document"
    doc2 = "This is a completely different second document"
    score = calculator.calculate_similarity(doc1, doc2)
    assert score < 1.0, "Different documents should have similarity score less than 1.0"
    assert score >= 0.0, "Similarity score should be non-negative"
    
    # Test partially similar documents
    doc1 = "This is a test document about machine learning"
    doc2 = "This is a test document about artificial intelligence"
    score = calculator.calculate_similarity(doc1, doc2)
    assert 0.0 < score < 1.0, "Partially similar documents should have score between 0 and 1"

def test_batch_similarity():
    calculator = SimilarityCalculator()
    
    documents = [
        "This is the first document",
        "This is the second document",
        "This is a completely different third document"
    ]
    
    similarity_matrix = calculator.batch_similarity(documents)
    
    # Check matrix shape
    assert similarity_matrix.shape == (3, 3), "Similarity matrix should be square"
    
    # Check diagonal elements (self-similarity)
    for i in range(3):
        assert similarity_matrix[i, i] == 1.0, "Self-similarity should be 1.0"
    
    # Check symmetry
    for i in range(3):
        for j in range(3):
            assert similarity_matrix[i, j] == similarity_matrix[j, i], "Similarity matrix should be symmetric" 