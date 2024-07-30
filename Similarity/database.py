

from typing import List, Dict, Tuple

class InvoiceDatabase:
    def __init__(self):
        self.invoices = []

    def add_invoice(self, invoice: Dict[str, any]):
        self.invoices.append(invoice)

    def find_most_similar(self, input_invoice: Dict[str, any], similarity_func) -> Tuple[Dict[str, any], float, str]:
        most_similar_invoice = None
        highest_similarity = 0.0
        most_similar_filename = None

        for invoice in self.invoices:
            similarity = similarity_func(input_invoice, invoice)
            if similarity > highest_similarity:
                highest_similarity = similarity
                most_similar_invoice = invoice
                most_similar_filename = invoice.get('filename')

        return most_similar_invoice, highest_similarity, most_similar_filename
