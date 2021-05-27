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
cat diamonds.csv | lvtab --y price
```

results:
```
tail_area_odds,lower_quantile,upper_quantile,lower_value,upper_value
4,0.25001,0.75001,950.0,5324.74999
8,0.12501,0.87501,694.0,8687.12499
16,0.06251,0.9375,572.0,12150.0625
32,0.03127,0.96875,497.0,14928.18749
64,0.01564,0.98438,449.0,16709.0
128,0.00782,0.9922,420.99218,17710.01561
256,0.00392,0.9961,394.0,18234.01561
512,0.00197,0.99805,376.0,18489.00779
1024,0.00099,0.99903,364.49901,18668.51071
2048,0.0005,0.99952,356.999,18741.0
```

`tail_area_odds` - odds are 1:x that a value is outside the range of the `lower_value` and `upper_value`
`*_quantile` - quantile of cut
`*_value` - the value of the cut at the given quantiles

See all options with `lvtab --help`

# Pair with `tv` for pretty printing

I have been working on [tv](https://github.com/alexhallam/tv) to make printing of csv files pretty in the command line. I use `lvtab` with `tv`.

```
cat diamonds.csv | lvtab --y price | tv
```

![lv](https://user-images.githubusercontent.com/9298693/119739666-8bf9d800-be50-11eb-8b79-236218e53af5.PNG)


# Installation

## Pip install

```
pip3 install lvtab
```



