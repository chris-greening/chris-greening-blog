# Author: Chris Greening
# Date: 2022-07-02
# Purpose: Sample code for cleaning and joining datasets using the tidyverse

library(readr)
library(purrr)
library(dplyr)
library(tibble)

setwd("C:/Users/chris/OneDrive - christophergreening.com/Documents/Programming/chris-greening-blog/posts/Performing multiple joins in R using dplyr and purrr/code")
source("process_data.R")

#### Load code maps ----
eu.agricultural.codes <- readr::read_csv("data/euro_agricultural_codes.csv") %>%
  select(Code, Description) %>%
  tibble::deframe()
eu.country.codes <- readr::read_csv("data/euro_country_codes.csv") %>%
  select(geo, country) %>%
  tibble::deframe()

#### Data processed, pivoted wide, and outer joined 
livestock.data <- list.files("data/eurostat_livestock_data/", full.names = TRUE) %>%
  purrr::map(function(fpath) {
    readr::read_csv(fpath) %>%
      .process.data(eu.agricultural.codes, eu.country.codes)
  }) %>%
  purrr::reduce(~dplyr::full_join(.x, .y, by=c("geo", "TIME_PERIOD")))


