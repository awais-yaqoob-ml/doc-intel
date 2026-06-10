# parsers/base.py

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BaseParser(ABC):
    """
    Base interface for all file parsers.
    """

    @abstractmethod
    def parse(self, file_path: str, **kwargs) -> Dict[str, Any]:
        """
        Parse file and return structured content.
        """
        raise NotImplementedError

    @abstractmethod
    def parse_bytes(self, file_bytes: bytes, **kwargs) -> Dict[str, Any]:
        """
        Parse raw bytes input.
        """
        raise NotImplementedError

    @abstractmethod
    def supported_formats(self) -> list[str]:
        """
        Return supported file extensions.
        """
        raise NotImplementedError