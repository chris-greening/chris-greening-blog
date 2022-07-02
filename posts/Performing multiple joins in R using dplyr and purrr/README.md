# Performing multiple joins in R using dplyr and purrr

Joining structured data on shared attributes is one of the most common tasks in data preparation

And while it's fine to hardcode our join statements for two or three tables, what happens when we want to join 10 tables? 1,000 tables?

This is where the reduce operation shines!

So let's jump right into some code and learn how we can leverage R and the tidyverse to write elegant and concise code that can join an arbitrary number of datasets 