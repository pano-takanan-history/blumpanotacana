library(tidyverse)
library(ggrepel)
library(rnaturalearth)
library(rnaturalearthdata)
library(viridis)

# Loading the data
lex <- read_csv('cldf/languages.csv')

# Downloading the map
spdf_sa <- ne_countries(continent=c("south america"),
                        scale="medium", 
                        returnclass="sf")

map_lex <- ggplot(data=lex) +
  geom_sf(data=spdf_sa) +
  coord_sf(ylim=c(-20, -2), xlim=c(-81, -59)) +
  geom_point(aes(
    Longitude,Latitude,
    fill=SubGroup, shape=SubGroup),
    size=4) +
  geom_label_repel(box.padding=0.8,
                   point.padding=0.5,
                  aes(Longitude, Latitude, label=Name), 
                   size=4,
                   max.overlaps=Inf) +
  labs(caption="Coordinates: Glottolog") +
  scale_shape_manual(values=c(21, 22, 23, 24, 25)) +
  scale_fill_viridis(begin=0, end=1, discrete=TRUE, option="D") +
  theme(legend.position="none")

map_lex
ggsave('fig_map.png', map_lex, units="px", width=2000, height=2000)
