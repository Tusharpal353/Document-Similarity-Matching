from text_extraction import extract_text_from_pdf
from feature_extraction import extract_features
from similarity_calculation import calculate_content_similarity, calculate_structural_similarity
from database import InvoiceDatabase
from structural_analysis import analyze_structure

def main(input_pdf_path, database):
    # Extract text and features from input PDF
    input_text = extract_text_from_pdf(input_pdf_path)
    input_features = extract_features(input_text)
    input_structure = analyze_structure(input_pdf_path)
    
    input_invoice = {'text': input_text, 'features': input_features, 'structure': input_structure}

    # Find the most similar invoice in the database
    similar_invoice, similarity_score = database.find_most_similar(input_invoice, calculate_content_similarity, calculate_structural_similarity)

    print(f"Most similar invoice: {similar_invoice}")
    print(f"Similarity score: {similarity_score}")

if __name__ == "__main__":
    db = InvoiceDatabase()
    # Add some sample invoices to the database
    sample_invoice_text = extract_text_from_pdf('path/to/sample_invoice.pdf')
    sample_invoice_features = extract_features(sample_invoice_text)
    sample_invoice_structure = analyze_structure('path/to/sample_invoice.pdf')
    db.add_invoice({'text': sample_invoice_text, 'features': sample_invoice_features, 'structure': sample_invoice_structure})

    # Run the main program with an input PDF
    main('path/to/input_invoice.pdf', db)
