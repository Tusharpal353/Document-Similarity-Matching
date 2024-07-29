from typing import Dict, Any
import re

def extract_features(text: str) -> Dict[str, Any]:
    # Basic keyword extraction
    keywords = set(re.findall(r'\b\w+\b', text.lower()))  # Simple word extraction
    return {'keywords': list(keywords)}
