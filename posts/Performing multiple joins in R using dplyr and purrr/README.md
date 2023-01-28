# Joining multiple datasets on the same column in R using dplyr and purrr

Joining multiple datasets on the same column is a common pattern in data preparation

So let's jump in and explore how we can leverage R and the tidyverse to join an arbitrary number of datasets on a shared column with elegant, readable code!

## Table of Contents 
- [Installing prerequisite packages](#installing-prerequisite-packages)
- [Examining our sample datasets](#examining-our-sample-datasets)
- [Using dplyr to manually join two datasets at a time](#using-dplyr)
- [Understanding the reduce operation](#understanding-the-reduce-operation)
- [Leveraging purrr to join multiple datasets](#leveraging-purrr-reduce)
- [Conclusion](#conclusion)
- [Additional resources](#additional-resources)

## Installing prerequisite packages
<a src="#installing-prerequisite-packages"></a>

In this tutorial we'll be using dplyr and purrr from the popular tidyverse collection of packages

The following line of code will install them on your machine if they aren't already:

```R
install.packages(c("dplyr", "purrr"))
```

## Examining our sample datasets
<a src="#examining-our-sample-datasets"></a>

For the following examples, we'll be using real-world agricultural data sourced via Eurostat containing the number of specific livestock animals (`swine`, `bovine`, `sheep`, and `goats`) in a `country` during a given `year`

For example, here is the `goats` dataset
```R
> goats
# A tibble: 1,322 × 3
   country  year goats
   <chr>   <dbl> <dbl>
 1 Albania  2014 904
 2 Albania  2015 932
 3 Albania  2016 941.
 4 Albania  2017 933.
 5 Albania  2018 917.
 6 Albania  2019 863.
 7 Albania  2020 774.
 8 Austria  1993  47
 9 Austria  1994  49.8
10 Austria  1995  54.2
# … with 1,312 more rows
```

Our goal is to join these datasets by `country` and `year` into a single `livestock.data` variable containing all the animals like so:

```R
> livestock.data
# A tibble: 1,322 × 6
   country  year bovine goats swine sheep
   <chr>   <dbl>  <dbl> <dbl> <dbl> <dbl>
 1 Albania  2014   500. 904    172. 1896
 2 Albania  2015   506. 932    177. 1918
 3 Albania  2016   497. 941.   184. 1972.
 4 Albania  2017   475. 933.   180. 1926.
 5 Albania  2018   467. 917.   184. 1864.
 6 Albania  2019   416. 863.   184. 1758.
 7 Albania  2020   363. 774.   158. 1558.
 8 Austria  1993  2334.  47     NA   334
 9 Austria  1994  2329.  49.8 3729.  342.
10 Austria  1995  2326.  54.2 3706.  365.
# … with 1,312 more rows
```

## Using dplyr::full_join to manually join two datasets at a time
<a src="#using-dplyr"></a>

Let's start with a naive approach and manually join our datasets one-by-one on the `country` and `year` columns

```R
by = c("country", "year")
livestock.data <- dplyr::full_join(bovine, goats, by=by)
livestock.data <- dplyr::full_join(livestock.data, swine, by=by)
livestock.data <- dplyr::full_join(livestock.data, sheep, by=by)
```

The above code accomplishes the exercise by:
1. Manually stepping through each animal
2. applying a function that takes two arguments (in this case `dplyr::full_join`)
3. and chaining the output of one step (`livestock.data`) as the input for the next step

While this might work for four datasets, what if we had 100 datasets? 1000 datasets? _n datasets?!_ Suddenly not a great solution! 

Let's investigate how we can improve, automate, and scale this

## Understanding the reduce operation
<a src="#understanding-the-reduce-operation"></a> 

The reduce operation is a technique that combines all the elements of an array (i.e. an array containing our individual livestock datasets) into a single value (i.e. the final joined table).   

The reduce operation accomplishes this by:
1. Looping over an array
2. applying a function that takes two arguments (such as `dplyr::full_join`) 
3. and chaining the output of one step as the input for the next step

Sound familiar? This is exactly what we just performed manually in the previous section except this time we'll be leveraging R to do it for us! 

So let's see in practice how we can apply the reduce operation to elegantly join our `livestock.data`

## Leveraging purrr::reduce to join multiple datasets
<a src="#leveraging-purrr-reduce"></a>

`purrr` is a package that enhances R's functional programming toolkit for working with functions and vectors (i.e. reducing, mapping, filtering, etc.)

In this case, we're going to use `purrr::reduce` in conjunction with `dplyr::full_join` to join all of our datasets in one line of concise, readable code

```R
livestock.data <- purrr::reduce(
    list(bovine, goats, swine, sheep),
    function(left, right) {
      dplyr::full_join(left, right, by=c("country", "year"))
    }
)
```

And that's it! We've joined all of our datasets in what's essentially a single line of code

Let's break down the arguments that we just passed to `purrr::reduce` 

First, we started with a list of our datasets:

```R
list(bovine, goats, swine, sheep)
```

And followed with a function that outer joins two datasets together 

```R
function(left, right) {
  dplyr::full_join(left, right, by=c("country", "year"))
}
```

## Conclusion
<a src="#conclusion"></a>

## Additional resources
<a src="#additional-resources"></a>
