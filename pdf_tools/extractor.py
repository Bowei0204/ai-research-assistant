# pdf_tools/extractor.py
import fitz  # PyMuPDF
import re

def extract_sections_from_pdf(filepath: str) -> dict:
    doc = fitz.open(filepath)
    full_text = "\n".join([page.get_text() for page in doc])
    doc.close()

    sections = {}
    patterns = [
        ("Abstract", r"(?i)(abstract)\s*[:\n]"),
        ("Introduction", r"(?i)(\n\d\.?\s*introduction)\s"),
        ("Methods", r"(?i)(\n\d\.?\s*(methods|methodology))\s")
    ]

    for i, (name, pattern) in enumerate(patterns):
        match = re.search(pattern, full_text)
        if match:
            start = match.end()
            end = len(full_text)
            for _, (_, next_pattern) in enumerate(patterns[i+1:], start=i+1):
                next_match = re.search(next_pattern, full_text[start:])
                if next_match:
                    end = start + next_match.start()
                    break
            sections[name] = full_text[start:end].strip()
        else:
            sections[name] = ""

    return sections
