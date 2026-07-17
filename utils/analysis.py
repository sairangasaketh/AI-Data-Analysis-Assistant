import pandas as pd


def get_dataset_summary(df):

    memory = round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2)

    return {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum()),
        "Memory Usage": f"{memory} MB",
    }


def get_missing_values(df):
    """Return missing values for each column."""
    missing = df.isnull().sum().reset_index()
    missing.columns = ["Column", "Missing Values"]
    return missing.sort_values(
        by="Missing Values",
        ascending=False
    )


def get_numeric_columns(df):
    """Return all numeric columns."""
    return df.select_dtypes(
        include=["number"]
    ).columns.tolist()


def get_categorical_columns(df):
    """Return all categorical columns."""
    return df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()


def get_dataset_health(df):

    total_cells = df.shape[0] * df.shape[1]

    if total_cells == 0:
        return {
            "Health Score": 0,
            "Status": "Empty Dataset"
        }

    missing = df.isnull().sum().sum()

    score = max(
        0,
        round((1 - missing / total_cells) * 100)
    )

    if score >= 95:
        status = "Excellent"
    elif score >= 80:
        status = "Good"
    elif score >= 60:
        status = "Fair"
    else:
        status = "Poor"

    return {
        "Health Score": score,
        "Status": status
    }

def get_statistics(df):
    """Return descriptive statistics."""
    return df.describe(include="all").fillna("")


def get_data_types(df):
    """Return data types of each column."""
    return pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str).values
    })


def get_duplicate_rows(df):
    """Return duplicate rows."""
    return df[df.duplicated()]


def get_unique_counts(df):
    """Return unique values count for each column."""
    return pd.DataFrame({
        "Column": df.columns,
        "Unique Values": df.nunique().values
    })