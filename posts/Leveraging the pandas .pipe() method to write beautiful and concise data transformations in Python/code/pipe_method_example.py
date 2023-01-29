# Author: Chris Greening
# Date: 2023-01-29
# Purpose: Sample code for processing European livestock data using pandas

from typing import Dict

import pandas as pd

def main() -> None:
    eu_agricultural_codes_df = _load_lookup_table("data/euro_agricultural_codes.csv", key_col="Code", val_col="Description")
    eu_country_codes_df = _load_lookup_table("data/euro_country_codes.csv", key_col="geo", val_col="country")

def _load_lookup_table(fpath: str, key_col: str, val_col: str) -> Dict[str, str]:
    """Return a dictionary key-val lookup table from CSV"""
    return (
        pd.read_csv(fpath)
        .set_index(key_col)
        [[val_col]]
        .to_dict()
        [val_col]
    )

if __name__ == "__main__":
    main()