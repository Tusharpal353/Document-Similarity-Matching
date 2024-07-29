""" from typing import Dict, Any

class InvoiceDatabase:
    def __init__(self):
        self.invoices = []

    def add_invoice(self, invoice: Dict[str, Any]):
        self.invoices.append(invoice)

    def find_most_similar(self, input_invoice: Dict[str, Any], similarity_function) -> (Dict[str, Any], float):
        best_match = None
        highest_similarity = 0.0
        for invoice in self.invoices:
            content_similarity = similarity_function(input_invoice['text'], invoice['text'])
            structural_similarity = similarity_function(input_invoice['features'], invoice['features'])
            overall_similarity = (content_similarity + structural_similarity) / 2
            if overall_similarity > highest_similarity:
                highest_similarity = overall_similarity
                best_match = invoice
        return best_match, highest_similarity
 """
 from typing import List, Dict, Tuple

class InvoiceDatabase:
    def __init__(self):
        self.invoices = []

    def add_invoice(self, invoice: Dict[str, any]):
        self.invoices.append(invoice)

    def find_most_similar(self, input_invoice: Dict[str, any], similarity_func) -> Tuple[Dict[str, any], float]:
        most_similar_invoice = None
        highest_similarity_score = 0.0

        for invoice in self.invoices:
            similarity_score = similarity_func(input_invoice, invoice)
            if similarity_score > highest_similarity_score:
                highest_similarity_score = similarity_score
                most_similar_invoice = invoice

        return most_similar_invoice, highest_similarity_score
