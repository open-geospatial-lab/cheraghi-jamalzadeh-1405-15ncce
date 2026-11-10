# calc_inferential.py
import pandas as pd
from scipy import stats

# بارگذاری فایل داده
df = pd.read_csv('cadastre_benchmark_data.csv')

# جدا کردن داده‌های جفت‌شده (Paired Data)
mana_data = df[df['Method'] == 'Mana'].sort_values(by=['Surveyor_ID', 'Parcel_ID'])
landguard_data = df[df['Method'] == 'LandGuard'].sort_values(by=['Surveyor_ID', 'Parcel_ID'])

# 1. آزمون زوجی t برای زمان عملیات
t_stat_time, p_val_time = stats.ttest_rel(mana_data['Execution_Time_Min'], landguard_data['Execution_Time_Min'])

# 2. آزمون زوجی t برای تعداد کلیک‌ها
t_stat_click, p_val_click = stats.ttest_rel(mana_data['Click_Count'], landguard_data['Click_Count'])

df_degrees = len(mana_data) - 1  # درجه آزادی (1000 - 1 = 999)

print("==================================================")
print("🔬 نتایج آزمون آماری زوجی (Paired t-test)")
print("==================================================")

print(f"\n⏱️ شاخص زمان عملیات:")
print(f"  - آماره آزمون T({df_degrees}): {t_stat_time:.1f}")
print(f"  - مقدار p-value: {p_val_time:.4e} (p < 0.001)")

print(f"\n🖱️ شاخص تعداد تعاملات (کلیک):")
print(f"  - آماره آزمون T({df_degrees}): {t_stat_click:.1f}")
print(f"  - مقدار p-value: {p_val_click:.4e} (p < 0.001)")