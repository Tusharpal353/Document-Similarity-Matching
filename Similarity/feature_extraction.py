import re

def extract_features(text):
    keywords = re.findall(r'\b\w+\b', text.lower())
    invoice_number = re.search(r'invoice number\s*:\s*(\S+)', text, re.IGNORECASE)
    date = re.search(r'date\s*:\s*(\S+)', text, re.IGNORECASE)
    amount = re.search(r'amount\s*:\s*(\S+)', text, re.IGNORECASE)

    return {
        'keywords': keywords,
        'invoice_number': invoice_number.group(1) if invoice_number else None,
        'date': date.group(1) if date else None,
        'amount': amount.group(1) if amount else None
    }

if __name__ == "__main__":
    text = "Your invoice text here"
    features = extract_features(text)
    print(features)
