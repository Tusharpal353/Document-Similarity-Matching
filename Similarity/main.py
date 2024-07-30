
from text_extraction import extract_text_and_structure_from_pdf
from feature_extraction import extract_features
from similarity_calculation import calculate_similarity
from database import InvoiceDatabase

def main(input_pdf_path, database):
    # Extract text and structure from input PDF
    input_data = extract_text_and_structure_from_pdf(input_pdf_path)
    input_text = input_data["text"]
    input_structure = input_data["structure"]
    input_features = extract_features(input_text, input_structure)
    input_invoice = {'text': input_text, 'features': input_features}

    # Find the most similar invoice in the database
    similar_invoice, similarity_score, similar_filename = database.find_most_similar(input_invoice, calculate_similarity)

    print(f"Most similar invoice: {similar_invoice}")
    print(f"Similarity score: {similarity_score}")
    print(f"Filename of the most similar invoice: {similar_filename}")

if __name__ == "__main__":
    db = InvoiceDatabase()

    # Add sample invoices to the database
    invoice_paths = [
        'invoices/invoice_102856.pdf',
        'invoices/invoice_77073.pdf',
        'invoices/2024.03.15_0954.pdf',
        'invoices/2024.03.15_1145.pdf',
        'invoices/Faller_8.pdf'
    ]

    for path in invoice_paths:
        invoice_data = extract_text_and_structure_from_pdf(path)
        invoice_text = invoice_data["text"]
        invoice_structure = invoice_data["structure"]
        invoice_features = extract_features(invoice_text, invoice_structure)
        db.add_invoice({'text': invoice_text, 'features': invoice_features, 'filename': path})

    # Run the main program with an input PDF
    main("invoices/Test/invoice_77098.pdf", db)
