library(tidyverse)
library(ggrepel)
library(rnaturalearth)
library(rnaturalearthdata)
library(viridis)


# Loading the data
langs <- read_csv('../cldf/languages.csv')

# Downloading the map
spdf_sa <- ne_countries(continent = c("south america"),
                        scale = "medium", 
                        returnclass = "sf")

map_lex <- ggplot(data=langs) +
  geom_sf(data = spdf_sa) +
  coord_sf(ylim=c(-22.5, 1), xlim= c(-82, -55)) +
  geom_point(aes(x=Longitude,y=Latitude, shape=SubGroup, fill=SubGroup), size=6) +
  geom_label_repel(box.padding=0.8,
                   point.padding=0.8,
                   aes(Longitude, Latitude, label=Name),
                   size=4,
                   max.overlaps = Inf) +
  scale_shape_manual(values =c("Pano"=21, "Tacana"=22, "Mosetén"=23, "Movima"=24, "Uru-Chipaya"=25)) +
  scale_fill_viridis_d(guide="legend", option="A") +
  labs(caption = "Data: Glottolog") +
  theme_bw() +
  theme(legend.position="bottom",
        axis.title = element_text(size = rel(1.3)),
        axis.text = element_text(size = rel(1.3)),
        legend.text = element_text(size = rel(1.3))) # +


ggsave('images/fig_map.png', map_lex, width=2400, height=3000, units="px")
