
from typing import Dict
import pdfplumber

def extract_text_and_structure_from_pdf(pdf_path: str) -> Dict[str, any]:
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        structural_elements = {
            "headers": [],
            "footers": [],
            "tables": []
        }
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text

            # Extract tables
            tables = page.extract_tables()
            if tables:
                structural_elements["tables"].extend(tables)

            # Example header/footer extraction
            # Customize this based on actual document layout
            header = page.extract_text(x_tolerance=2, y_tolerance=2, layout=False, crop=(0, 0, page.width, 50))
            footer = page.extract_text(x_tolerance=2, y_tolerance=2, layout=False, crop=(0, page.height - 50, page.width, page.height))

            if header:
                structural_elements["headers"].append(header)
            if footer:
                structural_elements["footers"].append(footer)

    return {
        "text": full_text,
        "structure": structural_elements
    }
