"""
مكتبة تحويل الأرقام إلى كلمات عربية بدقة نحوية.
الإصدار: 2.0.2

تدعم:
    - الأعداد من 0 إلى 20 منزلة
    - المذكر والمؤنث
    - العملات (ريال، جنيه، دينار، درهم، دولار)
    - المثنى والجمع والتمييز
    - الأعداد السالبة
    - الأعداد الترتيبية (الأول، الثاني، الثالث...)
    - التواريخ (ميلادي وهجري)
    - الوقت (الساعة والدقائق والثواني)
"""

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


# ============================================================
# قواميس الآحاد والعشرات والمئات (أصلية)
# ============================================================

ONES_MASCULINE = {
    0: "صفر", 1: "واحد", 2: "اثنان", 3: "ثلاثة", 4: "أربعة",
    5: "خمسة", 6: "ستة", 7: "سبعة", 8: "ثمانية", 9: "تسعة",
    10: "عشرة",
}

ONES_FEMININE = {
    0: "صفر", 1: "واحدة", 2: "اثنتان", 3: "ثلاث", 4: "أربع",
    5: "خمس", 6: "ست", 7: "سبع", 8: "ثمان", 9: "تسع",
    10: "عشر",
}

TEENS_MASCULINE = {
    11: "أحد عشر", 12: "اثنا عشر", 13: "ثلاثة عشر", 14: "أربعة عشر",
    15: "خمسة عشر", 16: "ستة عشر", 17: "سبعة عشر", 18: "ثمانية عشر",
    19: "تسعة عشر",
}

TEENS_FEMININE = {
    11: "إحدى عشرة", 12: "اثنتا عشرة", 13: "ثلاث عشرة", 14: "أربع عشرة",
    15: "خمس عشرة", 16: "ست عشرة", 17: "سبع عشرة", 18: "ثماني عشرة",
    19: "تسع عشرة",
}

TENS = {
    20: "عشرون", 30: "ثلاثون", 40: "أربعون", 50: "خمسون",
    60: "ستون", 70: "سبعون", 80: "ثمانون", 90: "تسعون",
}

HUNDREDS = {
    100: "مئة", 200: "مئتان", 300: "ثلاثمئة", 400: "أربعمئة",
    500: "خمسمئة", 600: "ستمئة", 700: "سبعمئة", 800: "ثمانمئة",
    900: "تسعمئة",
}

# المئات في حالة الإضافة (بحذف النون)
HUNDREDS_CONSTRUCT = {
    100: "مئة",
    200: "مئتا",
    300: "ثلاثمئة",
    400: "أربعمئة",
    500: "خمسمئة",
    600: "ستمئة",
    700: "سبعمئة",
    800: "ثمانمئة",
    900: "تسعمئة",
}


# ============================================================
# المقاييس الكبيرة
# ============================================================

SCALES = [
    (10**18, "كوينتليون", "كوينتليونان", "كوينتليونات", "كوينتليونًا"),
    (10**15, "كوادريليون", "كوادريليونان", "كوادريليونات", "كوادريليونًا"),
    (10**12, "تريليون", "تريليونان", "تريليونات", "تريليونًا"),
    (10**9,  "مليار", "ملياران", "مليارات", "مليارًا"),
    (10**6,  "مليون", "مليونان", "ملايين", "مليونًا"),
    (10**3,  "ألف", "ألفان", "آلاف", "ألفًا"),
]


# ============================================================
# العملات المدعومة
# ============================================================

CURRENCIES = {
    "SAR": {
        "name": "ريال", "dual": "ريالان", "plural": "ريالات",
        "accusative": "ريالاً",
        "fraction": "هللة", "fraction_plural": "هللات",
        "fraction_accusative": "هللة",
    },
    "EGP": {
        "name": "جنيه", "dual": "جنيهان", "plural": "جنيهات",
        "accusative": "جنيهًا",
        "fraction": "قرش", "fraction_plural": "قروش",
        "fraction_accusative": "قرشًا",
    },
    "KWD": {
        "name": "دينار", "dual": "ديناران", "plural": "دنانير",
        "accusative": "دينارًا",
        "fraction": "فلس", "fraction_plural": "فلوس",
        "fraction_accusative": "فلسًا",
    },
    "AED": {
        "name": "درهم", "dual": "درهمان", "plural": "دراهم",
        "accusative": "درهمًا",
        "fraction": "فلس", "fraction_plural": "فلوس",
        "fraction_accusative": "فلسًا",
    },
    "USD": {
        "name": "دولار", "dual": "دولاران", "plural": "دولارات",
        "accusative": "دولارًا",
        "fraction": "سنت", "fraction_plural": "سنتات",
        "fraction_accusative": "سنتًا",
    },
}


# ============================================================
# الأشهر الميلادية والهجرية
# ============================================================

MONTHS_GREGORIAN = {
    1: "يناير", 2: "فبراير", 3: "مارس", 4: "أبريل",
    5: "مايو", 6: "يونيو", 7: "يوليو", 8: "أغسطس",
    9: "سبتمبر", 10: "أكتوبر", 11: "نوفمبر", 12: "ديسمبر",
}

MONTHS_HIJRI = {
    1: "محرم", 2: "صفر", 3: "ربيع الأول", 4: "ربيع الآخر",
    5: "جمادى الأولى", 6: "جمادى الآخرة", 7: "رجب", 8: "شعبان",
    9: "رمضان", 10: "شوال", 11: "ذو القعدة", 12: "ذو الحجة",
}


# ============================================================
# الأعداد الترتيبية (Ordinal)
# ============================================================

ORDINAL_ONES_MASCULINE = {
    1: "الأول", 2: "الثاني", 3: "الثالث", 4: "الرابع",
    5: "الخامس", 6: "السادس", 7: "السابع", 8: "الثامن",
    9: "التاسع", 10: "العاشر",
}

ORDINAL_ONES_FEMININE = {
    1: "الأولى", 2: "الثانية", 3: "الثالثة", 4: "الرابعة",
    5: "الخامسة", 6: "السادسة", 7: "السابعة", 8: "الثامنة",
    9: "التاسعة", 10: "العاشرة",
}

ORDINAL_ONES_COMPOUND_MASCULINE = {
    1: "الحادي", 2: "الثاني", 3: "الثالث", 4: "الرابع",
    5: "الخامس", 6: "السادس", 7: "السابع", 8: "الثامن",
    9: "التاسع",
}

ORDINAL_ONES_COMPOUND_FEMININE = {
    1: "الحادية", 2: "الثانية", 3: "الثالثة", 4: "الرابعة",
    5: "الخامسة", 6: "السادسة", 7: "السابعة", 8: "الثامنة",
    9: "التاسعة",
}

ORDINAL_TEENS_MASCULINE = {
    11: "الحادي عشر", 12: "الثاني عشر", 13: "الثالث عشر",
    14: "الرابع عشر", 15: "الخامس عشر", 16: "السادس عشر",
    17: "السابع عشر", 18: "الثامن عشر", 19: "التاسع عشر",
}

ORDINAL_TEENS_FEMININE = {
    11: "الحادية عشرة", 12: "الثانية عشرة", 13: "الثالثة عشرة",
    14: "الرابعة عشرة", 15: "الخامسة عشرة", 16: "السادسة عشرة",
    17: "السابعة عشرة", 18: "الثامنة عشرة", 19: "التاسعة عشرة",
}

ORDINAL_TENS = {
    20: "العشرون", 30: "الثلاثون", 40: "الأربعون", 50: "الخمسون",
    60: "الستون", 70: "السبعون", 80: "الثمانون", 90: "التسعون",
}

ORDINAL_HUNDREDS = {
    100: "المئة", 200: "المئتان", 300: "الثلاثمئة", 400: "الأربعمئة",
    500: "الخمسمئة", 600: "الستمئة", 700: "السبعمئة", 800: "الثمانمئة",
    900: "التسعمئة",
}


# ============================================================
# الدوال المساعدة للأعداد الأصلية
# ============================================================

def _two_digits(number: int, feminine: bool = False) -> str:
    """تحوّل عددًا من 0 إلى 99 إلى كلمات."""
    if number <= 10:
        return (ONES_FEMININE if feminine else ONES_MASCULINE)[number]
    if 11 <= number <= 19:
        return (TEENS_FEMININE if feminine else TEENS_MASCULINE)[number]
    if number in TENS:
        return TENS[number]

    ones = number % 10
    tens = number - ones
    ones_word = (ONES_FEMININE if feminine else ONES_MASCULINE)[ones]
    return f"{ones_word} و{TENS[tens]}"


def _three_digits(number: int, feminine: bool = False, construct: bool = False) -> str:
    """تحوّل عددًا من 0 إلى 999 إلى كلمات.
    
    construct: إذا كان True، نستخدم صيغة الإضافة (مئتا بدل مئتان).
    """
    if number < 100:
        return _two_digits(number, feminine)

    hundreds = (number // 100) * 100
    remainder = number % 100

    if remainder == 0:
        return HUNDREDS_CONSTRUCT[hundreds] if construct else HUNDREDS[hundreds]

    hundreds_word = HUNDREDS_CONSTRUCT[hundreds] if construct else HUNDREDS[hundreds]
    return f"{hundreds_word} و{_two_digits(remainder, feminine)}"


def _effective_count(number: int) -> int:
    """
    ترجع العدد الفعلي الذي يحدد الصيغة النحوية للاسم التالي.
    """
    if number == 0:
        return 0

    temp = number
    while temp > 0:
        group = temp % 1000
        if group != 0:
            if group >= 100:
                last_two = group % 100
                return last_two if last_two != 0 else group
            return group
        temp //= 1000

    return 0


def _scale_form(count: int, scale: tuple) -> str:
    """ترجع الصيغة النحوية الصحيحة لاسم المقياس حسب العدد."""
    _, singular, dual, plural, accusative = scale

    if count == 1:
        return singular
    if count == 2:
        return dual
    if 3 <= count <= 10:
        return plural
    if 11 <= count <= 99:
        return accusative
    return singular


def _currency_form(count: int, currency: dict, is_fraction: bool = False) -> str:
    """ترجع الصيغة النحوية الصحيحة لاسم العملة حسب العدد."""
    if is_fraction:
        scale = (
            0,
            currency["fraction"],
            currency["fraction"],
            currency["fraction_plural"],
            currency["fraction_accusative"],
        )
    else:
        scale = (
            0,
            currency["name"],
            currency["dual"],
            currency["plural"],
            currency["accusative"],
        )
    return _scale_form(count, scale)


# ============================================================
# الدوال المساعدة للأعداد الترتيبية
# ============================================================

def _two_digits_ordinal(number: int, feminine: bool = False) -> str:
    """تحوّل عددًا من 1 إلى 99 إلى ترتيبي."""
    if number <= 10:
        return (ORDINAL_ONES_FEMININE if feminine else ORDINAL_ONES_MASCULINE)[number]
    if 11 <= number <= 19:
        return (ORDINAL_TEENS_FEMININE if feminine else ORDINAL_TEENS_MASCULINE)[number]
    if number in ORDINAL_TENS:
        return ORDINAL_TENS[number]

    ones = number % 10
    tens = number - ones

    if ones == 0:
        return ORDINAL_TENS[tens]

    ones_word = (
        ORDINAL_ONES_COMPOUND_FEMININE if feminine
        else ORDINAL_ONES_COMPOUND_MASCULINE
    )[ones]

    return f"{ones_word} و{ORDINAL_TENS[tens]}"


# ============================================================
# الدالة الرئيسية: to_arabic
# ============================================================

def to_arabic(number: int, feminine: bool = False) -> str:
    """
    تحوّل عددًا صحيحًا (حتى 20 منزلة) إلى كلمات عربية بدقة نحوية.

    أمثلة:
        >>> to_arabic(1234)
        'ألف ومئتان وأربعة وثلاثون'
        >>> to_arabic(200000)
        'مئتا ألف'
        >>> to_arabic(3, feminine=True)
        'ثلاث'
    """
    if not isinstance(number, int):
        raise TypeError("يجب أن يكون المدخل عددًا صحيحًا")

    MAX_20_DIGITS = 10**20 - 1
    if number > MAX_20_DIGITS:
        raise ValueError("الحد الأقصى هو 20 منزلة")

    if number < 0:
        return "سالب " + to_arabic(-number, feminine)

    if number == 0:
        return "صفر"

    parts = []
    remainder = number

    for scale in SCALES:
        scale_value = scale[0]
        if remainder >= scale_value:
            count = remainder // scale_value
            remainder = remainder % scale_value

            scale_name = _scale_form(count, scale)

            if count == 1:
                parts.append(scale_name)
            elif count == 2:
                parts.append(scale_name)
            else:
                # نمرر construct=True لأن العدد متبوع بمقياس
                count_words = _three_digits(count, feminine, construct=True)
                parts.append(f"{count_words} {scale_name}")

    if remainder > 0:
        parts.append(_three_digits(remainder, feminine, construct=False))

    return " و".join(parts)


# ============================================================
# دالة العملات: to_currency
# ============================================================

def to_currency(amount: float, code: str = "SAR", feminine: bool = False) -> str:
    """
    تحوّل مبلغًا ماليًا إلى كلمات عربية مع اسم العملة.

    أمثلة:
        >>> to_currency(1, "SAR")
        'ريال'
        >>> to_currency(200, "SAR")
        'مئتا ريال'
        >>> to_currency(1234.56, "SAR")
        'ألف ومئتان وأربعة وثلاثون ريالاً وست وخمسون هللة'
    """
    if code not in CURRENCIES:
        raise ValueError(f"العملة غير مدعومة: {code}. المدعوم: {list(CURRENCIES.keys())}")

    if not isinstance(amount, (int, float)):
        raise TypeError("يجب أن يكون المبلغ رقمًا")

    if amount < 0:
        return "سالب " + to_currency(-amount, code, feminine)

    currency = CURRENCIES[code]

    integer_part = int(amount)
    fraction_part = round((amount - integer_part) * 100)

    if fraction_part == 100:
        integer_part += 1
        fraction_part = 0

    parts = []

    if integer_part > 0:
        effective = _effective_count(integer_part)
        currency_word = _currency_form(effective, currency, is_fraction=False)

        if integer_part == 1:
            parts.append(currency_word)
        elif integer_part == 2:
            parts.append(currency_word)
        else:
            # نمرر construct=True لأن العدد متبوع باسم العملة
            words = _to_arabic_construct(integer_part, feminine)
            parts.append(f"{words} {currency_word}")

    if fraction_part > 0:
        effective = _effective_count(fraction_part)
        fraction_word = _currency_form(effective, currency, is_fraction=True)

        if fraction_part == 1:
            parts.append(fraction_word)
        elif fraction_part == 2:
            parts.append(fraction_word)
        else:
            # الكسور مؤنثة دائمًا
            words = _to_arabic_construct(fraction_part, feminine=True)
            parts.append(f"{words} {fraction_word}")

    if not parts:
        return "صفر"

    return " و".join(parts)


def _to_arabic_construct(number: int, feminine: bool = False) -> str:
    """
    نسخة من to_arabic تستخدم صيغة الإضافة للمئات.
    تُستخدم عندما يكون العدد متبوعًا باسم (عملة، مقياس...).
    """
    if number < 100:
        return _two_digits(number, feminine)

    if number < 1000:
        return _three_digits(number, feminine, construct=True)

    # للأعداد الكبيرة، نستخدم to_arabic العادية
    return to_arabic(number, feminine)


# ============================================================
# دالة الترتيب: to_ordinal
# ============================================================

def to_ordinal(number: int, feminine: bool = False) -> str:
    """
    تحوّل عددًا إلى ترتيبي عربي.

    أمثلة:
        >>> to_ordinal(1)
        'الأول'
        >>> to_ordinal(21)
        'الحادي والعشرون'
        >>> to_ordinal(100)
        'المئة'
    """
    if not isinstance(number, int):
        raise TypeError("يجب أن يكون المدخل عددًا صحيحًا")
    if number < 1:
        raise ValueError("الترتيب يبدأ من 1")

    if number < 100:
        return _two_digits_ordinal(number, feminine)

    if number < 1000:
        hundreds = (number // 100) * 100
        remainder = number % 100

        if remainder == 0:
            return ORDINAL_HUNDREDS[hundreds]

        return f"{ORDINAL_HUNDREDS[hundreds]} و{_two_digits_ordinal(remainder, feminine)}"

    return "ال" + to_arabic(number, feminine)


# ============================================================
# دالة التاريخ: to_date
# ============================================================

def to_date(year: int, month: int, day: int, hijri: bool = False) -> str:
    """
    تحوّل تاريخًا إلى كلمات عربية.

    أمثلة:
        >>> to_date(2026, 9, 11)
        'الحادي عشر من سبتمبر عام ألفان وستة وعشرون'
        >>> to_date(1448, 3, 1, hijri=True)
        'الأول من ربيع الأول عام ألف وأربعمئة وثمانية وأربعين'
    """
    if not (1 <= month <= 12):
        raise ValueError("الشهر يجب أن يكون بين 1 و 12")
    if not (1 <= day <= 31):
        raise ValueError("اليوم يجب أن يكون بين 1 و 31")

    months = MONTHS_HIJRI if hijri else MONTHS_GREGORIAN
    month_name = months[month]
    day_word = to_ordinal(day)
    year_word = to_arabic(year)

    return f"{day_word} من {month_name} عام {year_word}"


# ============================================================
# دالة التاريخ الترتيبي: to_ordinal_date
# ============================================================

def to_ordinal_date(year: int, month: int, day: int, hijri: bool = False) -> str:
    """
    تحوّل تاريخًا إلى صيغة ترتيبية عربية (بدون السنة).

    أمثلة:
        >>> to_ordinal_date(2026, 9, 11)
        'الحادي عشر من سبتمبر'
    """
    if not (1 <= month <= 12):
        raise ValueError("الشهر يجب أن يكون بين 1 و 12")
    if not (1 <= day <= 31):
        raise ValueError("اليوم يجب أن يكون بين 1 و 31")

    months = MONTHS_HIJRI if hijri else MONTHS_GREGORIAN
    month_name = months[month]
    day_word = to_ordinal(day)

    return f"{day_word} من {month_name}"


# ============================================================
# دالة الوقت: to_time
# ============================================================

def to_time(hour: int, minute: int = 0, second: int = 0, period: str = None) -> str:
    """
    تحوّل وقتًا إلى كلمات عربية.

    المعاملات:
        hour: الساعة (0-23).
        minute: الدقائق (0-59).
        second: الثواني (0-59).
        period: "صباحًا" أو "مساءً" (اختياري، يُحدد تلقائيًا).

    أمثلة:
        >>> to_time(11, 25, 43, "مساءً")
        'الحادية عشرة مساءً وخمسة وعشرون دقيقة وثلاثة وأربعون ثانية'
        >>> to_time(9, 0, 0, "صباحًا")
        'التاسعة صباحًا'
    """
    if not (0 <= hour <= 23):
        raise ValueError("الساعة يجب أن تكون بين 0 و 23")
    if not (0 <= minute <= 59):
        raise ValueError("الدقائق يجب أن تكون بين 0 و 59")
    if not (0 <= second <= 59):
        raise ValueError("الثواني يجب أن تكون بين 0 و 59")

    if period is None:
        if 0 <= hour < 12:
            period = "صباحًا"
        elif hour == 12:
            period = "ظهرًا"
        else:
            period = "مساءً"

    hour_12 = hour % 12
    if hour_12 == 0:
        hour_12 = 12

    hour_word = to_ordinal(hour_12, feminine=True)

    parts = [f"{hour_word} {period}"]

    if minute > 0:
        if minute == 1:
            parts.append("دقيقة واحدة")
        elif minute == 2:
            parts.append("دقيقتان")
        else:
            minute_word = to_arabic(minute)
            parts.append(f"{minute_word} دقيقة")

    if second > 0:
        if second == 1:
            parts.append("ثانية واحدة")
        elif second == 2:
            parts.append("ثانيتان")
        else:
            second_word = to_arabic(second)
            parts.append(f"{second_word} ثانية")

    return " و".join(parts)