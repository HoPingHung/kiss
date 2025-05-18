import pandas as pd
from scipy.stats import pointbiserialr, pearsonr

# 讀取資料
df = pd.read_excel("DATA_Kiss_count_gender_and_IQ.xlsx")

# 轉換性別為二元
df['Gender_binary'] = df['Gender'].apply(lambda x: 1 if x.lower() == 'male' else 0)

# 性別與接吻次數（Point-Biserial）
r_kiss, p_kiss = pointbiserialr(df['Gender_binary'], df['Kiss Count'])

# 性別與初吻年齡
r_age, p_age = pointbiserialr(df['Gender_binary'], df['Age of First Kiss'])

# IQ 與接吻次數（Pearson）
r_iq_kiss, p_iq_kiss = pearsonr(df['IQ'], df['Kiss Count'])

# IQ 與初吻年齡
r_iq_age, p_iq_age = pearsonr(df['IQ'], df['Age of First Kiss'])

# 輸出結果
print("性別與接吻次數: r =", round(r_kiss, 3), ", p =", round(p_kiss, 3))
print("性別與初吻年齡: r =", round(r_age, 3), ", p =", round(p_age, 3))
print("IQ與接吻次數:   r =", round(r_iq_kiss, 3), ", p =", round(p_iq_kiss, 3))
print("IQ與初吻年齡:   r =", round(r_iq_age, 3), ", p =", round(p_iq_age, 3))

