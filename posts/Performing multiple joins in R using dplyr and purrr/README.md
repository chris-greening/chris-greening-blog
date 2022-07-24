# Joining multiple datasets on the same column in R using dplyr and purrr

Joining multiple datasets on the same column is a common pattern in data preparation

So let's explore how we can leverage R and the tidyverse to join an arbitrary number of datasets on a shared column with elegant, readable code

## Table of Contents 

## Installing prerequisite packages

In this tutorial we'll be using dplyr and purrr from the popular tidyverse collection of packages

```R
install.packages(c("dplyr", "purrr"))
```

## Examining our sample datasets

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

Our goal is to join these datasets by `country` and `year` into a single `livestock.data` variable containing all the animals

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

Let's start with a manual, naive approach and manually join our datasets one-by-one

```R
by = c("country", "year")
livestock.data <- dplyr::full_join(bovine, goats, by=by)
livestock.data <- dplyr::full_join(livestock.data, swine, by=by)
livestock.data <- dplyr::full_join(livestock.data, sheep, by=by)
```

In the above code we chain the output of each join statement as input for the next - incrementally building our dataset

## Understanding the reduce operation

The reduce operation is a technique that combines all the elements of a vector into a single value by iteratively applying a function that takes two arguments and chaining the output of one iteration into the input of the next

Sound familiar? This is almost exactly what we just performed manually when building `livestock.data`! So let's see how we can apply reduce to elegantly join all of our datasets

## Leveraging purrr::reduce to join multiple datasets

purrr is a package that enhances R's functional programming toolkit for working with functions and vectors

In this case, we're able to access a reduce operator via purrr::reduce and use in conjunction with dplyr::full_join to join all of our datasets in effectively one line of code

```R
livestock.data <- purrr::reduce(
    list(bovine, goats, swine, sheep),
    ~ dplyr::full_join(.x, .y, by=c("country", "year"))
)
```


## Conclusion

## Additional resources