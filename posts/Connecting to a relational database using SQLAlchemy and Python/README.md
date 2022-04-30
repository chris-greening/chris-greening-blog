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
- [Understanding the SQLAlchemy Engine](#understanding-the-sqlalchemy-engine)
- [Creating the Engine]()
- [Deconstructing the database URL](#deconstructing-the-database-url)
- [Connecting to a local SQLite database](#connecting-to-a-local-sqlite-database)
- [(Optional) Connecting to a remote MySQL instance on Amazon RDS](#connecting-to-a-relational-database-using-sqlalchemy-and-python)
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

Now back to the analogy of motor vehicles when we turn on our engine it's often because we have a **destination** in mind that we want to drive to

To get there we have to know things like:
1. **how** are we getting there?
2. **where** are we going?
3. **what** additional info do we need?

And in the context of SQLAlchemy, this is where our **database URL** comes in

A typical database URL might look something (but not always exactly) like this:
`dialect+driver://username:password@host:port/database`

Feeding this to our instance of `Engine`, we're able to inform SQLAlchemy crucial information such as:
- `dialect+driver`: is our database MySQL, PostgreSQL, etc? what DBAPI should our `Engine` connect to?
- `username:password`: what credentials do we need to connect to our database?
- `host:port`: where is our database?
- `database`: what is the name of our database?

Let's take a look at a couple examples of what an actual database URL could look like:

```python
# Connect to a local SQLite database
DATABASE_URL = "sqlite:///spam.db'
```

```python
# Connect to a remote MySQL instance on Amazon RDS
DATABASE_URL = "mysql+pymysql://chris:pa$$w0rd@insert-your-database-name.abcdefgh.us-east-1.rds.amazonaws.com:3306/mydatabase"
```

For additional information and usecases regarding the database URL, feel free to check out some of the [official SQLAlchemy documentation](https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls) on the subject!

---

## Creating the Engine
<a src="#creating-the-engine"></a>

So now let's go ahead and actually **create the engine**!

```python
from sqlalchemy import create_engine
engine = create_engine(DATABASE_URL)
```

"Wait - _that's it_?"

Yeah!



---

## Connecting to a local SQLite database
<a src="#connecting-to-a-local-sqlite-database"></a>

---

## (Optional) Connecting to a remote MySQL instance on Amazon RDS
<a src="#connecting-to-a-remote-mysql-instance-on-amazon-rds"></a>

---

## Conclusion
<a src="#conclusion"></a>

---

## Additional resources
<a src="#additional-resources"></a>

