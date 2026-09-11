"""مكتبة تحويل الأرقام إلى كلمات عربية بدقة نحوية."""
from .core import (
    to_arabic,
    to_currency,
    to_ordinal,
    to_ordinal_date,
    to_date,
    to_time,
    CURRENCIES,
    MONTHS_GREGORIAN,
    MONTHS_HIJRI,
)

__version__ = "2.0.2"
__all__ = [
    "to_arabic",
    "to_currency",
    "to_ordinal",
    "to_ordinal_date",
    "to_date",
    "to_time",
    "CURRENCIES",
    "MONTHS_GREGORIAN",
    "MONTHS_HIJRI",
]