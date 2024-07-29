from text_extraction import extract_text_from_pdf
from feature_extraction import extract_features
from similarity_calculation import calculate_similarity
from database import InvoiceDatabase

def main(input_pdf_path, database):
    # Extract text and features from input PDF
    input_text = extract_text_from_pdf(input_pdf_path)
    input_features = extract_features(input_text)
    input_invoice = {'text': input_text, 'features': input_features}

    # Find the most similar invoice in the database
    similar_invoice, similarity_score = database.find_most_similar(input_invoice, calculate_similarity)

    print(f"Most similar invoice: {similar_invoice}")
    print(f"Similarity score: {similarity_score}")

if __name__ == "__main__":
    db = InvoiceDatabase()
    # Add some sample invoices to the database
    sample_invoice_text = extract_text_from_pdf('invoices/invoice_102856.pdf')
    sample_invoice_features = extract_features(sample_invoice_text)
    db.add_invoice({'text': sample_invoice_text, 'features': sample_invoice_features})

    # Run the main program with an input PDF
    main("invoices/invoice_102856.pdf", db)
