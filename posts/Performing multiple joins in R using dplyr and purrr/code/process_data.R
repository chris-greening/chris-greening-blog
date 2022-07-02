# Author: Chris Greening
# Date: 2022-07-02
# Purpose: Function(s) for processing the dataset into desired format

library(tidyr)
library(dplyr)

.process.data <- function(dataset, eu.agricultural.codes, eu.country.codes) {
  return(
    dataset %>%
      dplyr::select(geo, TIME_PERIOD, animals, OBS_VALUE) %>%
      dplyr::mutate(
        animals = eu.agricultural.codes[animals],
        geo = eu.country.codes[geo]
      ) %>%
      tidyr::pivot_wider(names_from = animals, values_from = OBS_VALUE)
  )
}