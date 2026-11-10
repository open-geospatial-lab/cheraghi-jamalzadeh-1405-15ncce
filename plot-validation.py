import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import arabic_reshaper
from bidi.algorithm import get_display

# ==========================================================
# ۱. تنظیم فونت نیتیو سیستم‌عامل مک (macOS)
# ==========================================================
# فونت Geeza Pro روی ۱۰۰٪ مک‌ها نصب است و حروف فارسی را کامل و بدون مربع رندر می‌کند
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Geeza Pro', 'Arial', 'DecoType Naskh', 'B Nazanin']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use("seaborn-v0_8-whitegrid")

# تابع تبدیل اعداد به فارسی برای جلوگیری از تداخل
def to_fa_num(text):
    text = str(text)
    fa_digits = {'0':'۰', '1':'۱', '2':'۲', '3':'۳', '4':'۴', '5':'۵', '6':'۶', '7':'۷', '8':'۸', '9':'۹', '%':'٪'}
    for en, fa_d in fa_digits.items():
        text = text.replace(en, fa_d)
    return text

def fa(text):
    """اصلاح اتصال حروف و راست‌به‌چپ"""
    reshaped = arabic_reshaper.reshape(to_fa_num(text))
    return get_display(reshaped)

# ==========================================================
# ۲. داده‌های ارزیابی
# ==========================================================
error_types = [
    "خودتقاطع چندضلعی",
    "کنترل نقاط تکراری",
    "دنگل",
    "هم‌پوشانی",
    "شکاف",
    "ناسازگاری اطلاعات توصیفی"
]

detection_rates = np.array([80, 100, 100, 60, 70, 70])
total_generated = 50
total_detected = 40
overall_rate = 80

# رنگ‌بندی
colors = ['#f39c12', '#27ae60', '#27ae60', '#e74c3c', '#f39c12', '#f39c12']

# ==========================================================
# ۳. رسم نمودار افقی
# ==========================================================
fig, ax = plt.subplots(figsize=(11, 6), dpi=300)

y = np.arange(len(error_types))
bars = ax.barh(y, detection_rates, color=colors, edgecolor="#2c3e50", linewidth=1.1, height=0.55)

# تنظیم محور عمودی (نام خطاها)
ax.set_yticks(y)
ax.set_yticklabels([fa(item) for item in error_types], fontsize=13, fontweight='bold')
ax.invert_yaxis()  # ترتیب از بالا به پایین

# تنظیم محور افقی (درصدها)
ax.set_xlim(0, 115)
ax.set_xticks(np.arange(0, 101, 20))
ax.set_xticklabels([fa(f"{n}%") for n in range(0, 101, 20)], fontsize=11)

ax.set_xlabel(fa("نرخ تشخیص خطا"), fontsize=14, fontweight="bold", labelpad=10)
ax.set_title(fa("ارزیابی نرخ تشخیص خطا در موتور اعتبارسنجی سامانه LandGuard"), fontsize=15, fontweight="bold", pad=20)

# ==========================================================
# ۴. درج درصدها روی میله‌ها
# ==========================================================
for bar, rate in zip(bars, detection_rates):
    ax.text(
        rate + 2.5,
        bar.get_y() + bar.get_height() / 2,
        fa(f"{rate}%"),
        va="center",
        ha="left",
        fontsize=12,
        fontweight="bold",
        color="#2c3e50"
    )

# ==========================================================
# ۵. خط مرجع ۱۰۰٪
# ==========================================================
ax.axvline(x=100, color="#27ae60", linestyle="--", linewidth=1.5, alpha=0.8)
# ax.text(100, len(error_types) - 0.1, fa("حد تشخیص کامل"), ha="center", va="bottom", fontsize=10, color="#27ae60")

# ==========================================================
# ۶. باکس خلاصه وضعیت در بالا سمت چپ (بدون همپوشانی)
# ==========================================================
summary_text = (
    f"نرخ تشخیص کلی: {overall_rate}%\n"
    f"{total_detected} خطای شناسایی‌شده از {total_generated} خطای ایجادشده"
)

ax.text(
    1.1, 0.20,
    fa(summary_text),
    transform=ax.transAxes,
    ha="center",
    va="center",
    fontsize=11,
    fontweight="bold",
    color="#1e8449",
    bbox=dict(
        boxstyle="round,pad=0.6",
        facecolor="#e8f8f5",
        edgecolor="#27ae60",
        linewidth=1.5
    )
)

# تمیزکاری کادر
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="x", linestyle="--", alpha=0.5)
ax.grid(axis="y", visible=False)

plt.tight_layout()

# ذخیره تصویر
plt.savefig("validation_chart_mac_fixed.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.show()

print("تصویر کاملاً سالم بدون هیچ مربعی ذخیره شد: validation_chart_mac_fixed.png")