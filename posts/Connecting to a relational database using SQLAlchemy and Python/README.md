![Connecting to a relational database using SQLAlchemy and Python. Shows code snippet for connecting to a database.](./media/title%20image.gif)

# Connecting to a relational database using SQLAlchemy and Python

---

Congratulations!

You've just created your first SQLite database

Or maybe you read my previous blog post on [deploying a free tier relational database with Amazon RDS](https://dev.to/chrisgreening/deploying-a-free-tier-relational-database-with-amazon-rds-3jd2) :wink:

I have no idea! But I do know that you have a fancy database and now you want to access it from the comfort of Python

So let's jump into some code and learn how we can leverage [SQLAlchemy's](https://www.sqlalchemy.org/) capabilities as "_The Database Toolkit for Python_" to connect to a database!

### Table of Contents
- [Understanding the SQLAlchemy Engine](#understanding-the-sqlalchemy-engine)
- [Deconstructing the database URL](#deconstructing-the-database-url)
- [Connecting to a local SQLite database](#connecting-to-a-local-sqlite-database)
- [(Optional) Connecting to a remote MySQL instance on Amazon RDS](#connecting-to-a-relational-database-using-sqlalchemy-and-python)
- [Conclusion](#conclusion)
- [Additional resources](#additional-resources)

---

## Understanding the SQLAlchemy Engine

As we all know the engine is the most important component when it comes to operating (most) motor vehicles

It's a complex machine that:
1. takes gasoline as an input
2. burns the gasoline
3. converts the resulting heat into mechanical work as an output

Just like with motor vehicles, the [Engine](https://docs.sqlalchemy.org/en/14/core/connections.html#sqlalchemy.engine.Engine) is the heart of our SQLAlchemy application

It's the lowest level object used by SQLAlchemy and it drives the conversation forward between our Python application and a database that only understands SQL

<a src="#understanding-the-sqlalchemy-engine"></a>



![Animation showing the different parts of a SQLAlchemy connection string](media/engine%20configuration.PNG)

---

## Deconstructing the database URL
<a src="#deconstructing-the-database-url"></a>
<!-- The most basic function of the Engine is to provide access to a Connection, which can then invoke SQL statements. To emit a textual statement to the database looks like: -->
![Animation showing the different parts of a SQLAlchemy connection string](./media/url%20connection%20string.gif)

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

