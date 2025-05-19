import pandas as pd
from scipy.stats import pointbiserialr, pearsonr
import math

# ============================
# Utility Functions
# ============================

def load_data(filepath):
    """
    Load the Excel dataset and convert gender into binary format if needed.
    Male = 1, Female = 0
    """
    try:
        df = pd.read_excel(filepath)
        if 'Gender_binary' not in df.columns:
            df['Gender_binary'] = df['Gender'].str.lower().map({'male': 1, 'female': 0})
        return df
    except Exception as e:
        raise RuntimeError(f"Data loading failed: {e}")

def compute_correlation(x, y, method='pearson'):
    """
    Compute correlation coefficient (r), t-value, and p-value
    using the specified method: 'pearson' or 'pointbiserial'.
    
    Returns:
        tuple: (r, t, p), all rounded to 3 decimal places
    """
    n = len(x)
    if method == 'pearson':
        r, p = pearsonr(x, y)
    elif method == 'pointbiserial':
        r, p = pointbiserialr(x, y)
    else:
        raise ValueError("method must be either 'pearson' or 'pointbiserial'")
    
    # Calculate t-value based on r
    t_val = r * math.sqrt(n - 2) / math.sqrt(1 - r**2) if abs(r) < 1 else float('inf')
    return round(r, 3), round(t_val, 3), round(p, 3)

def display_result(label, r, t, p):
    """
    Print the result in a clean and formatted style
    """
    print(f"[{label}]")
    print(f"  ➤ r = {r}, t = {t}, p = {p}")
    print("-" * 40)

# ============================
# Main Execution Block
# ============================

if __name__ == "__main__":
    # Set the file path of the dataset
    filepath = "DATA_Kiss_count_gender_and_IQ.xlsx"
    
    # Load data
    df = load_data(filepath)
    
    # Define analyses: each entry includes label, X, Y, and method type
    analyses = [
        ("Gender vs Kiss Count", df['Gender_binary'], df['Kiss Count'], 'pointbiserial'),
        ("Gender vs Age of First Kiss", df['Gender_binary'], df['Age of First Kiss'], 'pointbiserial'),
        ("IQ vs Kiss Count", df['IQ'], df['Kiss Count'], 'pearson'),
        ("IQ vs Age of First Kiss", df['IQ'], df['Age of First Kiss'], 'pearson'),
        ("Kiss Count vs Age of First Kiss", df['Kiss Count'], df['Age of First Kiss'], 'pearson')  # ✅ New line added
    ]

    # Run and display results for each analysis
    for label, x, y, method in analyses:
        r, t, p = compute_correlation(x, y, method)
        display_result(label, r, t, p)
