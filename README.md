# lvtab

Lettervalue tables from the command line.

```

```

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



