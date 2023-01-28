# Author: Chris Greening
# Date: 2022-07-02
# Purpose: Sample code for cleaning and joining datasets using tidyverse libraries

library(readr)
library(purrr)
library(dplyr)
library(tibble)
library(tidyr)

setwd("/set/your/working/directory/here")

#### Read lookup tables and deframe into named vectors ----
eu.agricultural.codes <- readr::read_csv("data/euro_agricultural_codes.csv") %>%
  dplyr::select(Code, Description) %>%
  tibble::deframe()
eu.country.codes <- readr::read_csv("data/euro_country_codes.csv") %>%
  dplyr::select(geo, country) %>%
  tibble::deframe()

#### Load data, use lookup tables to convert codes to useful names, pivot data wide, and outer join 
livestock.data <- list.files("data/eurostat_livestock_data/", full.names = TRUE) %>%
  purrr::map(function(fpath) {
    readr::read_csv(fpath) %>%
      dplyr::select(geo, TIME_PERIOD, animals, OBS_VALUE) %>%
      dplyr::mutate(
        animals = eu.agricultural.codes[animals],
        geo = eu.country.codes[geo]
      ) %>%
      tidyr::pivot_wider(names_from = animals, values_from = OBS_VALUE)
  }) %>%
  purrr::reduce(~dplyr::full_join(.x, .y, by=c("geo", "TIME_PERIOD")))
