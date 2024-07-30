from typing import Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(invoice1: Dict[str, any], invoice2: Dict[str, any]) -> float:
    text1 = invoice1['text']
    text2 = invoice2['text']

    # Create TF-IDF vectors for the invoices
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])

    # Calculate cosine similarity between the vectors
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]
