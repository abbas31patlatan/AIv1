"""Storage for third party API keys.

In a real project these keys would be loaded from a secure location. The example
here only demonstrates the structure and should not be used in production.
"""

from dataclasses import dataclass
import os


@dataclass
class APIKeys:
    """Container holding optional API keys for integrations."""

    openai_key: str | None = os.getenv("OPENAI_API_KEY")
    translation_key: str | None = os.getenv("TRANSLATION_API_KEY")


keys = APIKeys()
"""Default keys object used by the system."""
