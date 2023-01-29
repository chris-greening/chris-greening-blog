# Author: Chris Greening
# Date: 2023-01-29
# Purpose: Example showing how the pandas pipe method works

import pandas as pd

def main() -> None:
    chris_blog_posts_df = pd.read_csv("data/chris_blog_posts.csv")
    top_five_tags_df = (
        chris_blog_posts_df
        .pipe(_select_relevant_columns)
        .pipe(_explode_tags_column_into_rows)
        .pipe(_aggregate_sum_by_tag)
        .pipe(_filter_top_five_tags_by_view)
    )
    print(top_five_tags_df)

def _filter_top_five_tags_by_view(df: "pd.DataFrame") -> "pd.DataFrame":
    """Return DataFrame with only the top 5 rows filters"""
    return (
        df
        .sort_values("views", ascending=False)
        .head(5)
    )

def _select_relevant_columns(df: "pd.DataFrame") -> "pd.DataFrame":
    """Return DataFrame with only relevant columns selected"""
    return df[["likes", "comments", "views", "tags"]]

def _explode_tags_column_into_rows(df: "pd.DataFrame") -> "pd.DataFrame":
    """Return DataFrame with tags column exploded into separate rows"""
    df["tags"] = df["tags"].str.split(",")
    df = df.explode("tags")
    return df
    
def _aggregate_sum_by_tag(df: "pd.DataFrame") -> "pd.DataFrame":
    """Return DataFrame grouped by summed up to tag level"""
    return (
        df
        .groupby("tags", as_index=False)
        .sum()
    )

if __name__ == "__main__":
    main()