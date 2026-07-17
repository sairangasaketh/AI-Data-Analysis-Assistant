import re
import pandas as pd


class QueryEngine:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def execute(self, query: str):

        q = query.lower().strip()

        # ----------------------------
        # Dataset Information
        # ----------------------------

        if "rows" in q:
            return f"The dataset contains {len(self.df)} rows."

        if "columns" in q:
            return f"The dataset contains {len(self.df.columns)} columns: {', '.join(self.df.columns)}"

        if "shape" in q:
            return f"Dataset shape: {self.df.shape}"

        if "duplicate" in q:
            dup = self.df.duplicated().sum()
            return f"The dataset contains {dup} duplicate rows."

        if "missing" in q or "null" in q:
            missing = self.df.isnull().sum()
            return missing[missing > 0].to_string()

        # ----------------------------
        # Column Exists
        # ----------------------------

        for col in self.df.columns:

            if col.lower() in q:

                # Average

                if "average" in q or "mean" in q:

                    if pd.api.types.is_numeric_dtype(self.df[col]):

                        return f"Average of '{col}' = {self.df[col].mean():.2f}"

                # Maximum

                if "maximum" in q or "max" in q or "highest" in q:

                    if pd.api.types.is_numeric_dtype(self.df[col]):

                        return f"Maximum value of '{col}' = {self.df[col].max()}"

                # Minimum

                if "minimum" in q or "lowest" in q or "min" in q:

                    if pd.api.types.is_numeric_dtype(self.df[col]):

                        return f"Minimum value of '{col}' = {self.df[col].min()}"

                # Sum

                if "sum" in q or "total" in q:

                    if pd.api.types.is_numeric_dtype(self.df[col]):

                        return f"Sum of '{col}' = {self.df[col].sum()}"

                # Median

                if "median" in q:

                    if pd.api.types.is_numeric_dtype(self.df[col]):

                        return f"Median of '{col}' = {self.df[col].median()}"

                # Mode

                if "mode" in q:

                    return self.df[col].mode().to_string(index=False)

                # Unique values

                if "unique" in q:

                    return f"{col} has {self.df[col].nunique()} unique values."

                # Value counts

                if "count" in q:

                    return self.df[col].value_counts().head(10).to_string()

                # Standard deviation

                if "standard deviation" in q or "std" in q:

                    if pd.api.types.is_numeric_dtype(self.df[col]):

                        return f"Standard deviation of '{col}' = {self.df[col].std():.2f}"

                # Variance

                if "variance" in q:

                    if pd.api.types.is_numeric_dtype(self.df[col]):

                        return f"Variance of '{col}' = {self.df[col].var():.2f}"

        # ----------------------------
        # Correlation
        # ----------------------------

        if "correlation" in q:

            numeric = self.df.select_dtypes(include="number")

            if numeric.shape[1] >= 2:

                return numeric.corr().round(2).to_string()

        # ----------------------------
        # Describe
        # ----------------------------

        if "summary" in q or "describe" in q:

            return self.df.describe(include="all").to_string()

        # ----------------------------
        # Data Types
        # ----------------------------

        if "data type" in q or "dtype" in q:

            return self.df.dtypes.to_string()

        # ----------------------------
        # Memory Usage
        # ----------------------------

        if "memory" in q:

            mem = self.df.memory_usage(deep=True).sum() / (1024 ** 2)

            return f"Dataset memory usage: {mem:.2f} MB"

        # ----------------------------
        # Head
        # ----------------------------

        if "head" in q or "first rows" in q:

            return self.df.head().to_string()

        # ----------------------------
        # Tail
        # ----------------------------

        if "tail" in q or "last rows" in q:

            return self.df.tail().to_string()

        # ----------------------------
        # Not handled
        # ----------------------------

        return None