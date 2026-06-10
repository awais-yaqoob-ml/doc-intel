# ocr/detector.py

from typing import List, Dict, Tuple


class LayoutDetector:
    """
    Simple layout detection placeholder.
    Can be extended with YOLO/LayoutLM/DocLayNet later.
    """

    def detect_regions(self, image: bytes) -> List[Dict]:
        """
        Detect text regions in an image.
        Returns list of bounding boxes.
        """
        return [
            {
                "bbox": [0, 0, 100, 100],
                "type": "text",
                "confidence": 0.99,
            }
        ]

    def group_lines(self, ocr_boxes: List[Dict]) -> List[List[Dict]]:
        """
        Group OCR boxes into logical lines/blocks.
        """
        return [ocr_boxes]