# Author: Chris Greening
# Date: 2022-04-30
# Purpose: Supplementary example project for using SQLAlchemy
# to create, seed, and query a simple local SQLite database

import csv
from typing import List

import sqlalchemy
from sqlalchemy import create_engine, text

def main() -> None:
    engine = create_engine("sqlite:///test.db")
    with engine.connect() as connection:
        _create_table(connection)
        seed_data = _load_seed_data_from_csv("chris_blog_posts.csv")
        _insert_seed_data_into_table(connection=connection, seed_data=seed_data)
        _print_all_posts(connection=connection)
        _print_most_recent_post(connection=connection)
        _print_three_longest_posts(connection=connection)

def _create_table(connection: sqlalchemy.engine.base.Connection) -> None:
    """Create a table for persisting information about blog posts"""
    try:
        connection.execute(text("""
        CREATE TABLE chris_blog_posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title STRING,
            author STRING,
            date TEXT,
            word_count INTEGER
        )
    """))
    except sqlalchemy.exc.OperationalError:
        print("Table already exists!")

def _insert_seed_data_into_table(
        connection: sqlalchemy.engine.base.Connection,
        seed_data: List[List[str]]
    ) -> None:
    """Loop through seed data rows and insert into database"""
    queries = [_construct_insert_query(row) for row in seed_data[1:]]
    for query in queries:
        connection.execute(text(query))

def _print_all_posts(connection: sqlalchemy.engine.base.Connection) -> None:
    """Loop through every row and print title and author of blog post"""
    print("\nAll posts:")
    resp = connection.execute(text("SELECT title, author FROM chris_blog_posts"))
    for row in resp:
        print(f"\"{row['title']}\" by {row['author']}")

def _print_most_recent_post(connection: sqlalchemy.engine.base.Connection) -> None:
    print("\nThe most recent post:")
    resp = connection.execute(text("""
        SELECT title, date
        FROM chris_blog_posts
        ORDER BY date(date) DESC
        LIMIT 1
    """))
    for row in resp:
        print(f"The most recently published blog post was \"{row['title']}\" on {row['date']}")

def _print_three_longest_posts(connection: sqlalchemy.engine.base.Connection) -> None:
    print("\nThe three longest posts:")
    resp = connection.execute(text("""
        SELECT title, word_count
        FROM chris_blog_posts
        ORDER BY date(date) DESC
        LIMIT 3
    """))
    for row in resp:
        print(f"\"{row['title']}\" has {row['word_count']} words.")

def _construct_insert_query(row: List[str]) -> str:
    """Return a SQL INSERT statement for row of data"""
    title, author, date, word_count = row
    return f"""
        INSERT INTO chris_blog_posts (title, author, date, word_count)
        VALUES ("{title}", "{author}", date("{date}"), {word_count})
    """

def _load_seed_data_from_csv(fpath: str) -> List[List[str]]:
    """Return a list of lists of strings parsed from CSV to insert into database"""
    with open(fpath) as infile:
        return list(csv.reader(infile))

if __name__ == "__main__":
    main()
