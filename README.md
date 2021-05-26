# lvtab

Lettervalue tables from the command line.

# Introduction

The inspiration for this project came from the paper [Letter-value plots: Boxplots for large data](https://vita.had.co.nz/papers/letter-value-plot.pdf).

It seemed like a good idea to not just have these letter-values for plotting, but also in tabular for as summary statistics. This was how letter values
were originally introduced in to that world in [Exploratory Data Analysis](https://www.amazon.com/Exploratory-Data-Analysis-John-Tukey/dp/0201076160).
For some reason they did not seem to catch on. Maybe this was becase the data at the time was smaller. Modern petabyte sized data vindicates letter values.

This package aims to be a user friendly command line utility to generate these values.

# Features

1. Works with tidy data
2. Tukey inspired
3. Printable csv only - making a nice display in Cloudwatch or other logging tools
4. Uses data piped with stdout making it compatable with a wider range of unix tools.

# Example 

```
# download data
wget https://raw.githubusercontent.com/tidyverse/ggplot2/master/data-raw/diamonds.csv

# install lvtab
pip3 install lvtab 

# ungrouped lv table
cat diamonds.csv | lv --y price

```

See all options with `lv --help`

# Pair with `tv` for pretty printing

```
cat diamonds.csv | lv --y price | tv
```

# Installation

## Pip install

```
pip3 install lvtab
```



