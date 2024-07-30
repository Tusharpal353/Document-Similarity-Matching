# Invoice Similarity Project

## Overview

The Invoice Similarity Project aims to identify the most similar invoice from a database by comparing the text and structural information of an input invoice. This system leverages natural language processing (NLP) and machine learning techniques to calculate similarity scores between the input invoice and a database of invoices, thereby facilitating efficient invoice management and comparison.

## Approach

### Document Representation Method

1. **Text Extraction**: 
   - We use the `pdfplumber` library to extract text from PDF invoices.
   - Each PDF invoice is parsed to retrieve the textual content, which is essential for further processing.

2. **Feature Extraction**:
   - Key features such as invoice amounts, dates, phrases, and other relevant details are extracted using NLP techniques.
   - The extracted text is processed to identify important features that contribute to invoice similarity.

3. **Document Representation**:
   - Each invoice is represented by its extracted features. This representation allows us to quantify and compare invoices based on their content.

### Similarity Metric Used

- **Cosine Similarity**: 
   - Cosine similarity is employed to measure the similarity between feature vectors of the input invoice and each invoice in the database.
   - The cosine similarity metric is chosen due to its effectiveness in comparing high-dimensional data and capturing the similarity between document vectors.

### Workflow

1. **Input PDF Invoice**: Provide the path to the PDF invoice you wish to compare.
2. **Text and Structure Extraction**: The system extracts text and structural details from the PDF.
3. **Feature Extraction**: Key features are extracted from the invoice text.
4. **Database Comparison**: Compare the features of the input invoice against those in the invoice database.
5. **Similarity Score Calculation**: Compute similarity scores using cosine similarity.
6. **Output Results**: The most similar invoice and its similarity score are displayed.

## Results

### Demonstration Video
[Link text](https://www.loom.com/share/441909e4ded5448fa035e0e7c714fdbb?sid=63e4f4e6-a96e-4ec8-bb28-2b875e0cd6a2)

A video demonstrating the functionality of the code, including the input and comparison process, is available. The video shows:
- How the system processes and extracts features from an input invoice.
- The comparison of the input invoice with database invoices.
- The similarity scores and matched invoices.

### Example Results

- **Input Invoice**: `invoices/2024.03.15_1145.pdf`
  - **Matched Invoice**: `invoices/Faller_8.pdf`
  - **Similarity Score**: 0.89

- **Input Invoice**: `invoices/2024.07.15_2030.pdf`
  - **Matched Invoice**: `invoices/Smith_Invoice_1.pdf`
  - **Similarity Score**: 0.75

## Instructions

### How to Run the Project

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-repository/invoice-similarity.git
    cd invoice-similarity
    ```

2. **Set Up the Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Run the Main Script**:
    ```sh
    python main.py
    ```

4. **Prepare the Data**:
    - Place your input PDF invoice in the `Invoices/` directory.
    - Ensure that the database of invoices is placed in the specified directory and is correctly referenced in the code.

## Conclusion

The Invoice Similarity Project provides a robust solution for comparing invoices by leveraging advanced NLP techniques and similarity metrics. The system efficiently extracts and compares invoice features to identify the most similar documents, making it a valuable tool for managing and processing invoices.

For further details or inquiries, please refer to the demonstration video or contact us for additional information.

