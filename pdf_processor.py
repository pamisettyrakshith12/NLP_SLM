import fitz
import re


def extract_text_from_pdf(pdf_file):
    """
    Extract text from an uploaded PDF file.
    """

    document = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()
        text += "\n"

    document.close()

    return text


def extract_terms(text):
    """
    Extract glossary terms and definitions.

    Expected formats:
    Algorithm - A step-by-step procedure...
    Compiler: A program that translates...
    """

    lines = text.split("\n")

    terms = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        match = re.match(
            r"^(.+?)\s*[-:]\s*(.+)$",
            line
        )

        if match:

            term = match.group(1).strip()
            definition = match.group(2).strip()

            if (
                len(term) < 100
                and len(definition) > 5
            ):

                terms.append({
                    "term": term,
                    "definition": definition
                })

    return terms