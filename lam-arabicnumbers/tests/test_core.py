"""
اختبارات شاملة لمكتبة arabicnumbers.
تشغيل: pytest test_arabicnumbers.py -v
"""
import pytest
from lam_arabicnumbers import (
    to_arabic, to_currency, to_ordinal,
    to_ordinal_date, to_date, to_time,
    CURRENCIES, MONTHS_GREGORIAN, MONTHS_HIJRI,
)

# ============================================================
# 1. اختبارات to_arabic — الأساسيات (0-99)
# ============================================================

def test_zero():
    assert to_arabic(0) == "صفر"


def test_ones():
    assert to_arabic(1) == "واحد"
    assert to_arabic(2) == "اثنان"
    assert to_arabic(3) == "ثلاثة"
    assert to_arabic(5) == "خمسة"
    assert to_arabic(9) == "تسعة"
    assert to_arabic(10) == "عشرة"


def test_teens():
    assert to_arabic(11) == "أحد عشر"
    assert to_arabic(12) == "اثنا عشر"
    assert to_arabic(13) == "ثلاثة عشر"
    assert to_arabic(19) == "تسعة عشر"


def test_tens():
    assert to_arabic(20) == "عشرون"
    assert to_arabic(30) == "ثلاثون"
    assert to_arabic(40) == "أربعون"
    assert to_arabic(50) == "خمسون"
    assert to_arabic(60) == "ستون"
    assert to_arabic(70) == "سبعون"
    assert to_arabic(80) == "ثمانون"
    assert to_arabic(90) == "تسعون"


def test_compound():
    assert to_arabic(21) == "واحد وعشرون"
    assert to_arabic(25) == "خمسة وعشرون"
    assert to_arabic(44) == "أربعة وأربعون"
    assert to_arabic(99) == "تسعة وتسعون"


# ============================================================
# 2. اختبارات to_arabic — المئات (100-999)
# ============================================================

def test_hundreds():
    assert to_arabic(100) == "مئة"
    assert to_arabic(200) == "مئتان"
    assert to_arabic(300) == "ثلاثمئة"
    assert to_arabic(900) == "تسعمئة"


def test_hundreds_with_remainder():
    assert to_arabic(101) == "مئة وواحد"
    assert to_arabic(250) == "مئتان وخمسون"
    assert to_arabic(999) == "تسعمئة وتسعة وتسعون"


# ============================================================
# 3. اختبارات to_arabic — الآلاف
# ============================================================

def test_thousand_singular():
    assert to_arabic(1000) == "ألف"


def test_thousand_dual():
    assert to_arabic(2000) == "ألفان"


def test_thousand_plural():
    assert to_arabic(3000) == "ثلاثة آلاف"
    assert to_arabic(10000) == "عشرة آلاف"


def test_thousand_accusative():
    assert to_arabic(11000) == "أحد عشر ألفًا"
    assert to_arabic(99000) == "تسعة وتسعون ألفًا"


def test_thousand_hundreds():
    assert to_arabic(100000) == "مئة ألف"
    assert to_arabic(200000) == "مئتا ألف"
    # 999 >= 100، إذن نستخدم المفرد المجرد "ألف" وليس "ألفًا"
    assert to_arabic(999999) == "تسعمئة وتسعة وتسعون ألف وتسعمئة وتسعة وتسعون"

def test_thousand_compound():
    assert to_arabic(1234) == "ألف ومئتان وأربعة وثلاثون"
    assert to_arabic(1500) == "ألف وخمسمئة"
    assert to_arabic(1001) == "ألف وواحد"


# ============================================================
# 4. اختبارات to_arabic — الملايين والمليارات
# ============================================================

def test_million():
    assert to_arabic(10**6) == "مليون"
    assert to_arabic(2 * 10**6) == "مليونان"
    assert to_arabic(3 * 10**6) == "ثلاثة ملايين"
    assert to_arabic(11 * 10**6) == "أحد عشر مليونًا"
    assert to_arabic(100 * 10**6) == "مئة مليون"


def test_billion():
    assert to_arabic(10**9) == "مليار"
    assert to_arabic(2 * 10**9) == "ملياران"
    assert to_arabic(3 * 10**9) == "ثلاثة مليارات"


def test_trillion_and_above():
    assert to_arabic(10**12) == "تريليون"
    assert to_arabic(10**15) == "كوادريليون"
    assert to_arabic(10**18) == "كوينتليون"


def test_complex_large_numbers():
    result = to_arabic(123456789)
    assert "مليون" in result
    assert "ألف" in result

    result = to_arabic(10**20 - 1)
    assert "كوينتليون" in result


# ============================================================
# 5. اختبارات to_arabic — المذكر والمؤنث
# ============================================================

def test_feminine_ones():
    assert to_arabic(1, feminine=True) == "واحدة"
    assert to_arabic(2, feminine=True) == "اثنتان"
    assert to_arabic(3, feminine=True) == "ثلاث"
    assert to_arabic(10, feminine=True) == "عشر"


def test_feminine_teens():
    assert to_arabic(11, feminine=True) == "إحدى عشرة"
    assert to_arabic(13, feminine=True) == "ثلاث عشرة"
    assert to_arabic(15, feminine=True) == "خمس عشرة"


def test_feminine_compound():
    assert to_arabic(21, feminine=True) == "واحدة وعشرون"
    assert to_arabic(23, feminine=True) == "ثلاث وعشرون"


# ============================================================
# 6. اختبارات to_arabic — الأعداد السالبة
# ============================================================

def test_negative():
    assert to_arabic(-1) == "سالب واحد"
    assert to_arabic(-5) == "سالب خمسة"
    assert to_arabic(-100) == "سالب مئة"
    assert to_arabic(-1000) == "سالب ألف"


# ============================================================
# 7. اختبارات to_arabic — الأخطاء
# ============================================================

def test_type_error_string():
    with pytest.raises(TypeError):
        to_arabic("5")


def test_type_error_float():
    with pytest.raises(TypeError):
        to_arabic(5.5)


def test_value_error_too_large():
    with pytest.raises(ValueError):
        to_arabic(10**20)


# ============================================================
# 8. اختبارات to_currency — العملات
# ============================================================

def test_currency_singular():
    assert to_currency(1, "SAR") == "ريال"
    assert to_currency(1, "EGP") == "جنيه"
    assert to_currency(1, "KWD") == "دينار"


def test_currency_dual():
    assert to_currency(2, "SAR") == "ريالان"
    assert to_currency(2, "EGP") == "جنيهان"


def test_currency_plural():
    assert to_currency(3, "SAR") == "ثلاثة ريالات"
    assert to_currency(10, "SAR") == "عشرة ريالات"


def test_currency_accusative():
    assert to_currency(11, "SAR") == "أحد عشر ريالاً"
    assert to_currency(45, "SAR") == "خمسة وأربعون ريالاً"


def test_currency_hundreds():
    assert to_currency(100, "SAR") == "مئة ريال"
    assert to_currency(200, "SAR") == "مئتا ريال"
    assert to_currency(1000, "SAR") == "ألف ريال"


def test_currency_with_fraction():
    assert to_currency(1.50, "SAR") == "ريال وخمسون هللة"
    # "خمس" وليس "خمسة" لأن هللة مؤنثة
    assert to_currency(2.25, "SAR") == "ريالان وخمس وعشرون هللة"
    assert to_currency(1234.56, "SAR") == (
        "ألف ومئتان وأربعة وثلاثون ريالاً وست وخمسون هللة"
    )


def test_currency_zero():
    assert to_currency(0, "SAR") == "صفر"


def test_currency_negative():
    assert to_currency(-45, "SAR") == "سالب خمسة وأربعون ريالاً"


def test_currency_unsupported():
    with pytest.raises(ValueError):
        to_currency(100, "XYZ")


def test_currency_type_error():
    with pytest.raises(TypeError):
        to_currency("100", "SAR")


# ============================================================
# 9. اختبارات to_ordinal — الأعداد الترتيبية
# ============================================================

def test_ordinal_ones():
    assert to_ordinal(1) == "الأول"
    assert to_ordinal(2) == "الثاني"
    assert to_ordinal(3) == "الثالث"
    assert to_ordinal(10) == "العاشر"


def test_ordinal_feminine():
    assert to_ordinal(1, feminine=True) == "الأولى"
    assert to_ordinal(3, feminine=True) == "الثالثة"


def test_ordinal_teens():
    assert to_ordinal(11) == "الحادي عشر"
    assert to_ordinal(12) == "الثاني عشر"
    assert to_ordinal(15, feminine=True) == "الخامسة عشرة"


def test_ordinal_tens():
    assert to_ordinal(20) == "العشرون"
    assert to_ordinal(30) == "الثلاثون"


def test_ordinal_compound():
    assert to_ordinal(21) == "الحادي والعشرون"
    assert to_ordinal(22) == "الثاني والعشرون"
    assert to_ordinal(31) == "الحادي والثلاثون"
    assert to_ordinal(99) == "التاسع والتسعون"


def test_ordinal_compound_feminine():
    assert to_ordinal(21, feminine=True) == "الحادية والعشرون"


def test_ordinal_hundreds():
    assert to_ordinal(100) == "المئة"
    assert to_ordinal(200) == "المئتان"


def test_ordinal_hundreds_compound():
    assert to_ordinal(101) == "المئة والأول"
    assert to_ordinal(123) == "المئة والثالث والعشرون"


def test_ordinal_errors():
    with pytest.raises(ValueError):
        to_ordinal(0)
    with pytest.raises(TypeError):
        to_ordinal("1")


# ============================================================
# 10. اختبارات to_date — التواريخ
# ============================================================

def test_date_gregorian():
    result = to_date(2026, 9, 11)
    assert "الحادي عشر" in result
    assert "سبتمبر" in result
    assert "ألفان وستة وعشرون" in result


def test_date_hijri():
    result = to_date(1448, 3, 1, hijri=True)
    assert "الأول" in result
    assert "ربيع الأول" in result


def test_date_first_day():
    result = to_date(2026, 1, 1)
    assert result.startswith("الأول من يناير")


def test_date_errors():
    with pytest.raises(ValueError):
        to_date(2026, 13, 1)
    with pytest.raises(ValueError):
        to_date(2026, 1, 32)


# ============================================================
# 11. اختبارات to_ordinal_date
# ============================================================

def test_ordinal_date_gregorian():
    assert to_ordinal_date(2026, 9, 11) == "الحادي عشر من سبتمبر"
    assert to_ordinal_date(2026, 1, 1) == "الأول من يناير"
    assert to_ordinal_date(2026, 12, 31) == "الحادي والثلاثون من ديسمبر"


def test_ordinal_date_hijri():
    result = to_ordinal_date(1448, 3, 1, hijri=True)
    assert result == "الأول من ربيع الأول"


def test_ordinal_date_errors():
    with pytest.raises(ValueError):
        to_ordinal_date(2026, 13, 1)
    with pytest.raises(ValueError):
        to_ordinal_date(2026, 1, 32)


# ============================================================
# 12. اختبارات to_time — الوقت
# ============================================================

def test_time_full():
    result = to_time(11, 25, 43, "مساءً")
    assert result == "الحادية عشرة مساءً وخمسة وعشرون دقيقة وثلاثة وأربعون ثانية"


def test_time_hour_only():
    assert to_time(9, 0, 0, "صباحًا") == "التاسعة صباحًا"


def test_time_with_minutes():
    # 2 = 2 صباحًا (نظام 24 ساعة)
    result = to_time(2, 30)
    assert "الثانية صباحًا" in result
    assert "ثلاثون دقيقة" in result

    # 14 = 2 مساءً
    result = to_time(14, 30)
    assert "الثانية مساءً" in result


def test_time_with_seconds():
    result = to_time(5, 0, 15, "صباحًا")
    assert "الخامسة صباحًا" in result
    assert "خمسة عشر ثانية" in result


def test_time_noon():
    assert to_time(12, 0, 0) == "الثانية عشرة ظهرًا"


def test_time_midnight():
    assert to_time(0, 0, 0) == "الثانية عشرة صباحًا"


def test_time_auto_period():
    assert "صباحًا" in to_time(9, 0, 0)
    assert "مساءً" in to_time(15, 0, 0)
    assert "ظهرًا" in to_time(12, 0, 0)


def test_time_errors():
    with pytest.raises(ValueError):
        to_time(24, 0, 0)
    with pytest.raises(ValueError):
        to_time(12, 60, 0)
    with pytest.raises(ValueError):
        to_time(12, 0, 60)


# ============================================================
# 13. اختبارات القواميس الثابتة
# ============================================================

def test_currencies_count():
    assert len(CURRENCIES) == 5
    assert "SAR" in CURRENCIES
    assert "USD" in CURRENCIES


def test_months_gregorian():
    assert len(MONTHS_GREGORIAN) == 12
    assert MONTHS_GREGORIAN[1] == "يناير"


def test_months_hijri():
    assert len(MONTHS_HIJRI) == 12
    assert MONTHS_HIJRI[9] == "رمضان"


# ============================================================
# 14. اختبارات التكامل
# ============================================================

def test_integration_invoice():
    amount = to_currency(1234.56, "SAR")
    date = to_date(2026, 9, 11)
    time = to_time(14, 30, 0)

    assert "ريال" in amount
    assert "سبتمبر" in date
    assert "الثانية مساءً" in time


def test_integration_consistency():
    for _ in range(10):
        assert to_arabic(1234) == "ألف ومئتان وأربعة وثلاثون"
        assert to_ordinal(21) == "الحادي والعشرون"


# ============================================================
# 15. اختبارات الحالات الحدية
# ============================================================

def test_boundary_zero():
    assert to_arabic(0) == "صفر"
    assert to_currency(0, "SAR") == "صفر"


def test_boundary_one():
    assert to_arabic(1) == "واحد"
    assert to_ordinal(1) == "الأول"


def test_boundary_max():
    result = to_arabic(10**20 - 1)
    assert "كوينتليون" in result


def test_boundary_ten():
    assert to_arabic(10) == "عشرة"
    assert to_ordinal(10) == "العاشر"


def test_boundary_hundred():
    assert to_arabic(100) == "مئة"
    assert to_ordinal(100) == "المئة"


def test_boundary_thousand():
    assert to_arabic(1000) == "ألف"
    assert to_currency(1000, "SAR") == "ألف ريال"