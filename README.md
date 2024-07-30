# Invoice Similarity Project

## Overview
This project compares an input invoice (in PDF format) to a database of existing invoices to identify the most similar one based on content and structural similarity. The primary goal is to automate the process of finding duplicate or similar invoices, which can be useful for various applications such as fraud detection, record-keeping, and data analysis.

## Approach

### Document Representation Method
The chosen method for representing documents involves extracting both text and structural features from the PDF invoices. The process is as follows:
1. **Text Extraction**: Using `pdfplumber`, the text content of each invoice is extracted. This includes parsing the text from different sections of the invoice.
2. **Structural Features**: In addition to text, structural features such as the layout and positioning of text blocks are considered. These features help capture the overall format and structure of the invoice.

### Similarity Metric
The similarity between invoices is calculated using a combination of text similarity and structural similarity:
1. **Text Similarity**: Text similarity is computed using a variety of methods, including TF-IDF vectors and cosine similarity. This captures the content overlap between invoices.
2. **Structural Similarity**: Structural similarity is evaluated by comparing the layout and arrangement of text blocks. This ensures that invoices with similar formatting are identified as similar, even if the exact text content differs.

By combining these two aspects, the approach aims to provide a robust measure of similarity that accounts for both content and presentation.

## Installation

### Prerequisites
- Python 3.8 or higher
- `pdfplumber` for PDF text extraction
- Other dependencies listed in `requirements.txt`

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/invoice-similarity.git
   cd invoice-similarity
