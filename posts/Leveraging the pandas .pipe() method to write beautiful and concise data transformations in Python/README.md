# Leveraging the pandas .pipe() method to write beautiful and concise data transformations in Python

When it comes to data science and analysis, being able to prepare and transform our data is a critical component of any successful project

So let's learn how we can leverage the pandas `pipe` method in Python to abstract complex data transformations into easy-to-read, self documenting operations!

## Table of Contents 
- [Overview of the .pipe() method](#overview-of-the-pipe-method)
- [A concrete example of the pipe method](#a-more-concrete-example-of-the-pipe-method")
- [Conclusion](#conclusion)
- [Additional resources](#additional-resources)

{% embed https://www.christophergreening.com %}

---

## Overview of the .pipe() method <a src="#overview-of-the-pipe-method"></a>

```python
import pandas as pd
```

The `pipe` method allows us to chain `Series` and `DataFrame` data transformations together in a semantically continuous pipeline of inputs and outputs

It accomplishes this by leveraging Python's support for higher-order functions - the ability to pass a function as an argument to another function

Let's take a look at a simple example (*NOTE: assume the functions and `DataFrame` are pre-defined offscreen*):

```python
transformed_df = (
    df
    .pipe(_select_columns)
    .pipe(_multiply_columns_by_two)
    .pipe(_filter_segments)
)
```

The code snippet above shows each pipe method:
1. Inputting the output from the previous pipe
2. Performing a well-defined operation or transformation (i.e. selecting columns)
3. Chaining the output into the input of the next pipe

*Wait I still don't understand what this means!!! Can we take a look at a more concrete example?!*

No worries! Yeah - let's take a look at a more concrete example in the next section

---

## A concrete example of the pipe method
<a src="#a-more-concrete-example-of-the-pipe-method"></a>

Let's pretend we have a `DataFrame`, let's call it `town_df`, that contains weekly time-series data for every single town in the United States

```python
import pandas as pd
town_df = pd.read_csv("time_series_data_for_every_single_town_in_the_united_states.csv")
```

And let's say we want to perform these specific transformations in this specific order:
1. select relevant columns
2. filter date range
3. approximate missing values
4. map town to state
5. aggregate up to week and state
6. upsample week frequency to daily
7. interpolate daily values

*Wouldn't it be great if we could implement each of those steps as it's own self-contained function and then \*pipe\* those functions together in an explicitly obvious chain of transformations?...*

Well I'm glad you asked (:wink:)! Check this out:

```python
transformed_df = (
    df
    .pipe(_select_relevant_columns)
    .pipe(_filter_date_range)
    .pipe(_approximate_missing_values)
    .pipe(_map_town_to_state)
    .pipe(_aggregate_up_to_week_and_state)
    .pipe(_upsample_week_frequency_to_daily)
    .pipe(_interpolate_daily_values)
)
```

And that's it! 

A clear and concise chain of immediately obvious data transformations - let's talk about some of the benefits of writing our code like this

## The maintainability benefits of using the pipe method

You may have noticed that I did not explicitly reveal to you the reader the implementation details of the piped functions

And yet you probably didn't have a hard time understanding (at least from a top-level view) of what transformations were taking place behind the scenes!

I bet you could even show this to someone that has never written a single line of code in their life and even they'd be able to get the overall gist of what's happening to the dataset

While some simple transformations can be accomplished in a single line of code, more complex transformations might take dozens, hundreds, or even thousands of lines before we can move onto the "next" transformation

```python
transformed_df = (
    df
    .pipe(_some_oneliner_transformation)
    .pipe(_some_million_lines_of_code_transformation_but_guess_what_you_dont_have_to_know_how_it_works_all_you_have_to_know_is_its_expected_output)
)
```

So being able to abstract the implementation details under a well-defined unit or block of code removes the cognitive overhead of having to read *every single line* to know what's going on - you can just focus on the big picture (which is often the most important part)

##  <a src="#conclusion"></a>


---

## Conclusion <a src="#conclusion"></a>

---

## Additional resources <a src="#additional-resources"></a>

