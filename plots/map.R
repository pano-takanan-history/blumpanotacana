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
  coord_sf(ylim=c(-20.5, 2), xlim= c(-80, -45)) +
  geom_point(aes(x=Longitude,y=Latitude, shape=Subgroup, fill=Subgroup), size=10) +
  scale_shape_manual(values=c("Pano"=21, "Tacana"=22, "Mosetén"=23, "Movima"=24, "Uru-Chipaya"=25)) +
  scale_fill_viridis_d(guide="legend", option="D") +
  labs(caption = "Data: Glottolog") +
  theme_bw() +
  theme(legend.position="right",
        axis.title = element_text(size = rel(1.3)),
        axis.text = element_text(size = rel(1.3)),
        legend.text = element_text(size = rel(1.5)),
        legend.spacing.y = unit(0.5, 'cm'),
        legend.spacing.x = unit(0.2, 'cm'),
        legend.title = element_text(size = rel(0))) +
  guides(shape = guide_legend(byrow = TRUE))

map_lex
ggsave('fig_map.png', map_lex, units="px", width=5000, height=2000)
