library(readr)
library(dplyr)
library(tidyr)


data <- read_tsv('datasets/blumpanotacana/raw/raw.tsv')

data %>% group_by(DOCULECT, CONCEPT, TOKENS) %>% count() %>% filter(n>1) %>% 
  arrange(DOCULECT, CONCEPT)
