

from typing import Dict
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def extract_features(text: str, structure: Dict[str, any]) -> Dict[str, any]:
    words = text.lower().split()
    keywords = [word for word in words if word not in ENGLISH_STOP_WORDS]
    return {
        "keywords": keywords,
        "headers": structure["headers"],
        "footers": structure["footers"],
        "tables": structure["tables"],
        "invoice_number": None,
        "date": None,
        "amount": None
    }
