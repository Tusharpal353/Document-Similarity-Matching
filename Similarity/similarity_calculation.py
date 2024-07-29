from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    return cosine_similarity(vectors)[0, 1]

if __name__ == "__main__":
    text1 = "Sample text 1"
    text2 = "Sample text 2"
    similarity = calculate_similarity(text1, text2)
    print(f"Similarity: {similarity}")
