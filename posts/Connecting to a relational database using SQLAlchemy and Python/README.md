![Connecting to a relational database using SQLAlchemy and Python. Shows code snippet for connecting to a database.](./media/title%20image.gif)

# Connecting to a relational database using SQLAlchemy and Python

---

Welcome!

Perhaps you've just created your first SQLite database.

Or maybe you read my previous blog post on [deploying a free tier relational database with Amazon RDS](https://dev.to/chrisgreening/deploying-a-free-tier-relational-database-with-amazon-rds-3jd2) :wink:

{% embed https://dev.to/chrisgreening/deploying-a-free-tier-relational-database-with-amazon-rds-3jd2 %}

In however way you've arrived here - *welcome*!

And now that you've got that fancy database I'm _sure_ you just can't wait to access it from the warm embrace of **Python**.

So let's jump into some code and learn how we can leverage [SQLAlchemy's](https://www.sqlalchemy.org/) capabilities as "_The Database Toolkit for Python_" to connect to our database!

### Table of Contents
<a src="#table-of-contents"></a>
- [Understanding the SQLAlchemy Engine](#understanding-the-sqlalchemy-engine)
- [Creating the Engine]()
- [Deconstructing the database URL](#deconstructing-the-database-url)
- [Executing a SQL query from Python](#executing-a-sql-query-from-python)
- [Conclusion](#conclusion)
- [Additional resources](#additional-resources)

_:exclamation: IMPORTANT :exclamation:: This tutorial is strictly for **practical learning purposes** and NOT an exhaustive guide for setting up a secure production-ready environment._

_Be sure to keep an eye out for additional :exclamation: IMPORTANT :exclamation: notes throughout this tutorial for **potential security concerns, gotchas, etc**_.

---

## Understanding the SQLAlchemy Engine
<a src="#understanding-the-sqlalchemy-engine"></a>

As we all know the engine is the **heart** of (most) motor vehicles.

It's a complex machine that:
1. takes gasoline as an **input**
2. burns the gasoline
3. and converts the resulting heat into mechanical work as an **output**

And just like with motor vehicles, the [`Engine`](https://docs.sqlalchemy.org/en/14/core/connections.html#sqlalchemy.engine.Engine) is the **heart** of SQLAlchemy.

It's the **lowest level object** used by SQLAlchemy and it helps **drive** the conversation between our Python application and database(s).

![Image showing the different layers between the database and our connection](media/engine%20configuration.PNG)

Without going into too much detail, the `Engine`
internally references a:
- [`Dialect`](https://docs.sqlalchemy.org/en/14/dialects/) object that handles **communication** and a
- [`Pool`](https://docs.sqlalchemy.org/en/14/core/pooling.html#sqlalchemy.pool.Pool) object that handles **connection**.

These in turn work with the [DBAPI](https://docs.sqlalchemy.org/en/14/glossary.html#term-DBAPI) behind the scenes to **translate information** to and from our app and database.

The `Engine` is a complex piece of software that:
1. takes **input** from our Python app
2. processes the information
3. and converts it into **output** that our SQL database can understand

Don't sweat the details when you're first learning! :sweat_smile:

The important part here is just understanding that we have to **create** that **engine** for our app to use

## Deconstructing the database URL
<a src="#deconstructing-the-database-url"></a>

![Animation showing the different parts of a SQLAlchemy connection string](./media/url%20connection%20string.gif)

Now back to the analogy of motor vehicles... when we turn on our engine it's often because we have a **destination** in mind that we want to drive to

To get there we have to know things like:
1. **How** are we getting there?
2. **Where** are we going?
3. **What** additional information do we need?

And in the context of SQLAlchemy, this is where our **database URL** comes in

A typical **database URL** might look something (but not exactly) like this:
`dialect+driver://username:password@host:port/database`

Feeding this to our instance of `Engine`, we're able to inform SQLAlchemy crucial information such as:
- `dialect+driver`: Is our database **MySQL, PostgreSQL, etc**? what **DBAPI** should our `Engine` connect to?
- `username:password`: What **credentials** do we need to connect to our database?
- `host:port`: **Where** is our database?
- `database`: What is the **name** of our database?

So now let's take a look at a couple examples of what an **actual database URL** could look like:

```python
# Connect to a local SQLite database
DATABASE_URL = "sqlite:///spam.db'
```

```python
# Connect to a remote MySQL instance on Amazon RDS
DATABASE_URL = "mysql+pymysql://chris:pa$$w0rd@insert-your-database-name.abcdefgh.us-east-1.rds.amazonaws.com:3306/mydatabase"
```

```python
# Connect to a remote PostgreSQL database and pass additional parameters
DATABASE_URL = "postgresql+pg8000://user:pa$$w0rd@12.34.56.789/mydatabase?charset=utf8mb4
```

For **additional information** and usecases regarding the database URL, feel free to check out some of the [official SQLAlchemy documentation](https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls) on the subject!

_:exclamation: IMPORTANT :exclamation:: Publicly exposing your database to the internet and/or establishing unencrypted connections opens up **attack vectors** that make your database and application **vulnerable**._

_Reminder that this tutorial is **NOT** an exhaustive guide for setting up a secure production environment._

---

## Creating the Engine
<a src="#creating-the-engine"></a>

So now let's go ahead and actually **create the engine**!

```python
from sqlalchemy import create_engine
engine = create_engine(DATABASE_URL)
```

"Wait - _that's it_?"

Yeah! That's it!

It's worth mentioning that `Engine` (and more specifically the internal `Pool`) have a **lazy initialization**. They don't establish that first DBAPI connection until we explicitly [`connect`](https://docs.sqlalchemy.org/en/14/core/connections.html#sqlalchemy.engine.Engine.connect) or call an operation that uses `connect` internally such as [`execute`](https://docs.sqlalchemy.org/en/14/core/connections.html#sqlalchemy.engine.Connection.execute)

For **additional information** and usecases regarding `create_engine`, feel free to check out some of the [official SQLAlchemy documentation](https://docs.sqlalchemy.org/en/14/core/engines.html) on the subject!

---

## Executing a SQL query from Python
<a src="#executing-a-sql-query-from-python"></a>

And now that we've instantiated our `Engine`, we're ready to use it to **query our database** and parse its response into **usable data** in Python!

```python
from sqlalchemy import text

# Loop through every row in table chris_greenings_blog
with engine.connect() as connection:
    query = text("SELECT * FROM chris_greenings_blog")
    blog_posts = connection.execute(query)
    for post in blog_posts:
        print(post["title"])
```

In the above code snippet our `Engine` (and its internal references) have:
- established a **connection** to our database
- **translated** our Python textual `str` query into something the DBAPI can understand
- **executed** the query
- **returned and translated** the DBAPI's response into something Python can understand
- **looped through each row** and printed the title of every blog post

Pretty nifty, eh?

---

## Try it yourself!

As an addition to this blog post, I've **published a small project** on GitHub that uses SQLAlchemy to:
- create a local SQLite **database**
- create a **table**
- **seed** the database with data from a CSV
- perform simple **queries**

![Sample code that uses SQLAlchemy](./media/sample_code.PNG)

[Click here to check it out](https://github.com/chris-greening/chris-greening-blog/blob/main/posts/Connecting%20to%20a%20relational%20database%20using%20SQLAlchemy%20and%20Python/code/main.py) and be sure to tinker around with the code to get the most out of this tutorial!

---

## Conclusion
<a src="#conclusion"></a>

In this tutorial we covered one of the most critical aspects of using SQLAlchemy: _connecting to our database_

And this only scratched the surface of what we can accomplish with SQLAlchemy - I highly recommend **digging deeper** and learning more about what SQLAlchemy has to offer (such as its capabilities as an [Object Relational Mapper](https://docs.sqlalchemy.org/en/14/orm/))!

Thanks so much for reading and if you liked my content, be sure to check out some of my other work or connect with me on social media or my [personal website](https://www.christophergreening.com/) :smile:

Cheers!

[Back to the top :arrow_heading_up:](#table-of-contents)

{% embed https://dev.to/chrisgreening/deploying-a-free-tier-relational-database-with-amazon-rds-3jd2 %}

---

## Additional resources
<a src="#additional-resources"></a>

- [SQLAlchemy Official Website](https://www.sqlalchemy.org/)
- [Python Flask Tutorial: Full-Featured Web App Part 4 - Databaes with Flask-SQLAlchemy (Youtube)](https://www.youtube.com/watch?v=cYWiDiIUxQc&ab_channel=CoreySchafer)
- [SQLAlchemy - Python Tutorial](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91)
- [SQLAlchemy Github](https://github.com/sqlalchemy/sqlalchemy)
- [SQLAlchemy Tutorial](https://www.tutorialspoint.com/sqlalchemy/index.htm)
