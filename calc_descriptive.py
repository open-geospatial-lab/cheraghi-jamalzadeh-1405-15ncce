# calc_descriptive.py
import pandas as pd
import numpy as np

# بارگذاری فایل داده
df = pd.read_csv('cadastre_benchmark_data.csv')


def get_stats(data):
    mean_val = np.mean(data)
    sd_val = np.std(data, ddof=1)
    median_val = np.median(data)
    q75, q25 = np.percentile(data, [75, 25])
    iqr_val = q75 - q25
    return mean_val, sd_val, median_val, iqr_val


print("==================================================")
print("📊 آمار توصیفی شاخص‌ها (Descriptive Statistics)")
print("==================================================")

for method in ['Mana', 'LandGuard']:
    sub_df = df[df['Method'] == method]

    # زمان
    t_mean, t_sd, t_med, t_iqr = get_stats(sub_df['Execution_Time_Min'])
    # کلیک
    c_mean, c_sd, c_med, c_iqr = get_stats(sub_df['Click_Count'])

    print(f"\n🔹 روش: {method}")
    print(f"  ⏱️ زمان کل عملیات (دقیقه):")
    print(f"     - میانگین ± انحراف معیار: {t_mean:.1f} ± {t_sd:.1f}")
    print(f"     - میانه (IQR): {t_med:.1f} ({t_iqr:.1f})")

    print(f"  🖱️ تعداد تعاملات (کلیک):")
    print(f"     - میانگین ± انحراف معیار: {c_mean:.1f} ± {c_sd:.1f}")
    print(f"     - میانه (IQR): {c_med:.1f} ({c_iqr:.1f})")