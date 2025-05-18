import pandas as pd
from scipy.stats import pointbiserialr, pearsonr, t
import math

# Read data
df = pd.read_excel("DATA_Kiss_count_gender_and_IQ.xlsx")

# Added Gender binary conversion (male=1, female=0)
df['Gender_binary'] = df['Gender'].apply(lambda x: 1 if x.lower() == 'male' else 0)

# Sample number n
n = len(df)

def compute_t_stat(r, n):
    """給定相關係數與樣本數，計算 t 值"""
    return r * math.sqrt(n - 2) / math.sqrt(1 - r**2) if r**2 != 1 else float('inf')

def print_result(label, r_val, p_val):
    t_val = compute_t_stat(r_val, n)
    print(f"{label}: r = {r_val:.3f}, t = {t_val:.3f}, p = {p_val:.3f}")

# Gender vs Kiss Count
r1, p1 = pointbiserialr(df['Gender_binary'], df['Kiss Count'])
print_result("性別 vs 接吻次數", r1, p1)

# Gender vs. Age of First Kiss
r2, p2 = pointbiserialr(df['Gender_binary'], df['Age of First Kiss'])
print_result("性別 vs 初吻年齡", r2, p2)

# IQ vs Kiss Count（Pearson）
r3, p3 = pearsonr(df['IQ'], df['Kiss Count'])
print_result("IQ vs 接吻次數", r3, p3)

# IQ vs. Age of First Kiss
r4, p4 = pearsonr(df['IQ'], df['Age of First Kiss'])
print_result("IQ vs 初吻年齡", r4, p4)
