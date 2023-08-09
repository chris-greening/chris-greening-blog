# Author: Chris Greening
# Date: 2023-08-2023
# Purpose: Load a shapefile and visualize it

# install.packages(c("sf", "ggplot2", "tidyverse"))

library(sf)
library(ggplot2)
library(dplyr)

setwd("/path/to/working/directory")

shape.data <- sf::st_read("data/NUTS_RG_01M_2021_3035.shp") %>% 
  dplyr::filter(CNTR_CODE == "IT")
ggplot2::ggplot(data = shape.data) +
  ggplot2::geom_sf() +
  ggplot2::labs(title = "Italian NUTS-3 regions") +
  ggplot2::theme(
    panel.background = ggplot2::element_blank(),
    axis.text = ggplot2::element_blank(),
    axis.title = ggplot2::element_blank(),
    axis.ticks = ggplot2::element_blank(),
    legend.position = "none"
  )
