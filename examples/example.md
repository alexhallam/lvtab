```
# download data
wget https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv

# install lvtab
pip3 install lvtab  

# make box plots from data
cat mpg_ggplot2.csv | lv --g class --y hwy
``
