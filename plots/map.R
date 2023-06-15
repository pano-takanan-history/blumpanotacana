library(tidyverse)
library(ggrepel)
library(rnaturalearth)
library(rnaturalearthdata)
library(viridis)

# Loading the data
lex <- read_csv('../cldf/languages.csv') %>% 
  mutate(Subgroup = SubGroup)

# Downloading the map
spdf_sa <- ne_countries(continent=c("south america"),
                        scale="medium", 
                        returnclass="sf")

map_lex <- ggplot(data=lex) +
  geom_sf(data = spdf_sa) +
  coord_sf(ylim=c(-22.5, 1), xlim= c(-82, -55)) +
  geom_point(aes(x=Longitude,y=Latitude, shape=Subgroup, fill=Subgroup), size=6) +
  geom_label_repel(box.padding=0.8,
                   point.padding=0.8,
                   aes(Longitude, Latitude, label=Name),
                   size=4,
                   max.overlaps = Inf) +
  scale_shape_manual(values=c("Pano"=21, "Tacana"=22, "Mosetén"=23, "Movima"=24, "Uru-Chipaya"=25)) +
  scale_fill_viridis_d(guide="legend", option="D") +
  labs(caption = "Data: Glottolog") +
  theme_bw() +
  theme(legend.position="bottom",
        axis.title = element_text(size = rel(1.3)),
        axis.text = element_text(size = rel(1.3)),
        legend.text = element_text(size = rel(1.3))) 

map_lex
ggsave('fig_map.png', map_lex, units="px", width=3000, height=2000)
