# Author: Chris Greening
# Date: 2023-02-04
# Purpose: Example showing the MultiIndex in practice

import pandas as pd

def main() -> None:
    sales_df = pd.read_csv("sales_data.csv")
    multiiindex = _create_multiindex(sales_df)
    sales_df = _reindex_dataframe(sales_df, multiiindex)
    print(sales_df)


def _create_multiindex(sales_df: "pd.DataFrame") -> "pd.MultiIndex":
    """Return a MultiIndex created from the unique combinations of the month,
    product, and region columns in sales_df
    """
    names = ["month", "region", "product"]
    unique_categories = [sales_df[name].unique() for name in names]
    multiindex = pd.MultiIndex.from_product(
        unique_categories,
        names = names
    )
    return multiindex

def _reindex_dataframe(sales_df: "pd.DataFrame", multiindex: "pd.MultiIndex") -> "pd.DataFrame":
    """Return sales_df reindexed to align with multiiindex completing any missing
    combinations and filling them with zero
    """
    sales_df = (
        sales_df
        .set_index(multiindex.names)
        .reindex(multiindex, fill_value=0)
        .reset_index()
    )
    return sales_df

if __name__ == "__main__":
    main()