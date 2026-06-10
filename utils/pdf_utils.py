# utils/pdf_utils.py

from typing import List


def estimate_page_count(pdf_bytes: bytes) -> int:
    """
    Naive PDF page count estimator (stub).
    Replace with PyMuPDF or pdfplumber.
    """
    return max(1, len(pdf_bytes) // 5000)


def split_pdf_pages(pdf_bytes: bytes) -> List[bytes]:
    """
    Stub: simulate splitting PDF into pages.
    """
    page_count = estimate_page_count(pdf_bytes)
    return [pdf_bytes for _ in range(page_count)]