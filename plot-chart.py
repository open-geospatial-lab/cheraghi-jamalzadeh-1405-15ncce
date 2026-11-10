import matplotlib.pyplot as plt
import matplotlib
import arabic_reshaper
from bidi.algorithm import get_display
# import shutil

# # This deletes the Matplotlib cache directory
# shutil.rmtree(matplotlib.get_cachedir())

# تابع اصلاح راست‌به‌چپ و اتصالات حروف فارسی
def fa(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

# Step 1: Set the global font family (e.g., 'serif', 'sans-serif', 'monospace')
plt.rcParams['font.family'] = 'sans-serif'

# Step 2: Define specific fonts to look for (ordered by preference)
plt.rcParams['font.sans-serif'] = ['XB Niloofar','Helvetica', 'Arial', 'DejaVu Sans']

# Step 2: Define specific fonts to look for (ordered by preference)
# plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'DejaVu Sans']
# تنظیم استایل گرافیکی
plt.style.use('seaborn-v0_8-whitegrid')
categories = [fa('سامانه مانا\n(پس‌پردارزش)'), fa('سامانه LandGuard\n(بلادرنگ)')]
colors = ['#7f8c8d', '#27ae60']  # خاکستری برای مانا، سبز برای LandGuard

# ==========================================
# 📊 پلات اول: زمان اجرای عملیات
# ==========================================
fig1, ax1 = plt.subplots(figsize=(6, 5), dpi=300)

time_means = [10.2, 6.1]
time_std = [1.8, 0.9]

bars1 = ax1.bar(categories, time_means, yerr=time_std, capsize=8, color=colors, width=0.45, edgecolor='black', alpha=0.9)

ax1.set_ylabel(fa('میانگین زمان عملیات (دقیقه)'), fontsize=12, fontweight='bold')
ax1.set_title(fa('ارزیابی زمان عملیات\np < 0.001 , t(999) = 79.6'), fontsize=13, fontweight='bold', pad=15)
ax1.set_ylim(0, 15)

# نمایش عدد میانگین داخل هر ستون
for bar, mean in zip(bars1, time_means):
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, yval / 2, f'{mean} min', ha='center', va='center', color='white', fontweight='bold', fontsize=12)

# باکس راهنما و میزان بهبود
ax1.annotate(fa('۴۰.۲٪ کاهش زمان\n(۴.۱ دقیقه سریع‌تر)'), xy=(1, 6.1), xytext=(0.55, 12),
            arrowprops=dict(facecolor='#c0392b', shrink=0.08, width=2, headwidth=7),
            ha='center', fontsize=11, fontweight='bold', color='#c0392b',
            bbox=dict(boxstyle="round,pad=0.4", fc="#fadbd8", ec="#c0392b", lw=1.5))

plt.tight_layout()
plt.savefig('chart_execution_time.png', dpi=300, bbox_inches='tight')
plt.show() # نمایش پلات اول


# ==========================================
# 📊 پلات دوم: تعداد تعاملات (کلیک)
# ==========================================
fig2, ax2 = plt.subplots(figsize=(6, 5), dpi=300)

click_means = [28.4, 19.8]
click_std = [4.2, 2.6]

bars2 = ax2.bar(categories, click_means, yerr=click_std, capsize=8, color=colors, width=0.45, edgecolor='black', alpha=0.9)

ax2.set_ylabel(fa('میانگین تعداد کلیک (تعاملات)'), fontsize=12, fontweight='bold')
ax2.set_title(fa('ارزیابی تعداد تعاملات (کلیک)\np < 0.001 , t(999) = 67.0'), fontsize=13, fontweight='bold', pad=15)
ax2.set_ylim(0, 40)

# نمایش عدد میانگین داخل هر ستون
for bar, mean in zip(bars2, click_means):
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, yval / 2, f'{mean} clicks', ha='center', va='center', color='white', fontweight='bold', fontsize=12)

# باکس راهنما و میزان بهبود
ax2.annotate(fa('۳۰.۳٪ کاهش کلیک\n(۸.۶ کلیک کمتر)'), xy=(1, 19.8), xytext=(0.55, 32),
            arrowprops=dict(facecolor='#c0392b', shrink=0.08, width=2, headwidth=7),
            ha='center', fontsize=11, fontweight='bold', color='#c0392b',
            bbox=dict(boxstyle="round,pad=0.4", fc="#fadbd8", ec="#c0392b", lw=1.5))

plt.tight_layout()
plt.savefig('chart_user_clicks.png', dpi=300, bbox_inches='tight')
plt.show() # نمایش پلات دوم

print("هر دو پلات به‌صورت جداگانه با بالاترین کیفیت ذخیره شدند.")
