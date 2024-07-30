# Invoice Similarity Project

## Overview

This project aims to identify the most similar invoice from a database by comparing the text and structural information of an input invoice. By leveraging natural language processing (NLP) and machine learning techniques, we calculate similarity scores between the input invoice and the invoices in the database to find the best match.

## Approach

### Step-by-Step Workflow

1. **Input PDF Invoice**: The process begins with the input of a PDF invoice.
2. **Text and Structure Extraction**: We use `pdfplumber` to extract the text and structural information from the PDF invoice.
3. **Feature Extraction**: The extracted text is processed to extract features such as key phrases, amounts, dates, and other relevant information using NLP techniques.
4. **Input Features**: The features extracted from the input invoice are prepared for comparison.
5. **Database Comparison**: The input features are compared against the features of each invoice in the database.
6. **Database Invoice Processing**: Each invoice in the database undergoes text extraction, feature extraction, and similarity score calculation.
7. **Similarity Score Calculation**: The similarity score between the input invoice and each database invoice is calculated using cosine similarity and other relevant metrics.
8. **Compare Similarity Scores**: The similarity scores are compared to identify the most similar invoice.
9. **Output Results**: The results, including similarity scores and the matched invoices, are output.

### Flowchart of the Approach

```mermaid
graph TD
    A[Start] --> B[Input PDF Invoice]
    B --> C[Extract Text and Structure]
    C --> D[Extract Features]
    D --> E[Input Features]

    E --> F{Compare with Database}
    F --> G[Database Invoice 1]
    F --> H[Database Invoice 2]
    F --> I[Database Invoice N]

    G --> J[Extract Text and Structure]
    J --> K[Extract Features]
    K --> L[Database Features]
    L --> M[Calculate Similarity Score]
    M --> N[Similarity Score for Invoice 1]

    H --> O[Extract Text and Structure]
    O --> P[Extract Features]
    P --> Q[Database Features]
    Q --> R[Calculate Similarity Score]
    R --> S[Similarity Score for Invoice 2]

    I --> T[Extract Text and Structure]
    T --> U[Extract Features]
    U --> V[Database Features]
    V --> W[Calculate Similarity Score]
    W --> X[Similarity Score for Invoice N]

    N --> Y{Compare Similarity Scores}
    S --> Y
    X --> Y
    Y --> Z[Most Similar Invoice]
    Z --> AA[Output Results]
    AA --> AB[End]
