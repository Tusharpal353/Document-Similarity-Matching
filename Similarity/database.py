class InvoiceDatabase:
    def __init__(self):
        self.invoices = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def find_most_similar(self, input_invoice, similarity_func):
        highest_similarity = 0
        most_similar_invoice = None
        for invoice in self.invoices:
            similarity = similarity_func(input_invoice['text'], invoice['text'])
            if similarity > highest_similarity:
                highest_similarity = similarity
                most_similar_invoice = invoice
        return most_similar_invoice, highest_similarity

if __name__ == "__main__":
    db = InvoiceDatabase()
    sample_invoice = {'text': 'Sample invoice text', 'features': {}}
    db.add_invoice(sample_invoice)
    print(db.invoices)
