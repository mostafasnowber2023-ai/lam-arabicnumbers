"""اختبار سريع لمكتبة lam_arabicnumbers."""
from lam_arabicnumbers import (
    to_arabic, to_currency, to_ordinal,
    to_date, to_ordinal_date, to_time,
)

print("=" * 60)
print("  اختبار سريع لمكتبة lam-arabicnumbers")
print("=" * 60)

# 1. الأعداد
print("\n--- to_arabic ---")
print(f"  1234       → {to_arabic(1234)}")
print(f"  200000     → {to_arabic(200000)}")
print(f"  3 (مؤنث)   → {to_arabic(3, feminine=True)}")

# 2. العملات
print("\n--- to_currency ---")
print(f"  45 SAR     → {to_currency(45, 'SAR')}")
print(f"  1234.56 SAR → {to_currency(1234.56, 'SAR')}")

# 3. الترتيب
print("\n--- to_ordinal ---")
print(f"  1          → {to_ordinal(1)}")
print(f"  21         → {to_ordinal(21)}")
print(f"  3 (مؤنث)   → {to_ordinal(3, feminine=True)}")

# 4. التاريخ
print("\n--- to_date ---")
print(f"  2026/9/11  → {to_date(2026, 9, 11)}")

# 5. التاريخ الترتيبي
print("\n--- to_ordinal_date ---")
print(f"  2026/9/11  → {to_ordinal_date(2026, 9, 11)}")

# 6. الوقت
print("\n--- to_time ---")
print(f"  11:25:43   → {to_time(11, 25, 43, 'مساءً')}")

print("\n" + "=" * 60)
print("  ✅ كل الدوال تعمل بنجاح!")
print("=" * 60)