import numpy as np
import pandas as pd


def save_to_csv(df, filename):
    """
    Write the pandas DataFrame to a CSV file.
    """
    df.to_csv(filename, index=False)

def range_to_text(df, columns):
    """
    Map numeric values in specified columns onto intensity levels.
    [1-2: Minimal, 3-4: Mild, 5-6: Moderate, 7-8: Severe, 9-10: Critical]
    """
    df = df.copy()

    def classify(score):
        if pd.isna(score):
            return np.nan
        elif 0 <= score <= 2.5:
            return "Minimal"
        elif 2.5 < score <= 4.5:
            return "Mild"
        elif 4.5 < score <= 6.5:
            return "Moderate"
        elif 6.5 < score <= 8.5:
            return "Severe"
        elif 8.5 < score <= 10:
            return "Critical"
        else:
            return "Invalid"

    for col in columns:
        df.loc[:, col + "_label"] = df[col].apply(classify)

    return df

def handling_missing_values(df):
    """
    Impute missing values:
    - For numerical columns: use mean if symmetric, median if skewed.
    - For non-numerical/text columns: use mode.
    """
    df = df.copy()

    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if pd.api.types.is_numeric_dtype(df[col]):
                col_skew = df[col].skew(skipna=True)
                if abs(col_skew) < 0.5:
                    df[col] = df[col].fillna(df[col].mean())
                else:
                    df[col] = df[col].fillna(df[col].median())
            else:
                mode_val = df[col].mode()
                if not mode_val.empty:
                    df[col] = df[col].fillna(mode_val[0])
    return df

def handle_duplicates(df):
    """
    Locate and drop duplicate rows.
    """
    df = df.drop_duplicates().copy()
    return df

def drop_irrelevant_columns(df, columns):
    """
    Drop specified columns from the DataFrame.
    """
    df = df.drop(columns=columns, errors='ignore').copy()
    return df