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
  # coord_sf(ylim=c(-55, 10), xlim= c(-88.5, -35)) +
  geom_point(aes(x=Longitude,y=Latitude, shape=Family, color=Family),
             size=5) +
  # geom_label_repel(box.padding=1,
  #                  point.padding = 0.3,
  #                  aes(Longitude, Latitude, label=Name),
  #                  size=4,
  #                  max.overlaps = Inf) +
  # scale_shape_manual(values =c("Mayoruna"=21, "Panoan"=22, "Tacanan"=24)) +
  scale_fill_viridis_d(guide = "legend") +
  # labs(caption = "Data: Glottolog") +
  theme_bw() +
  theme(legend.position="bottom",
        axis.title = element_text(size = rel(1.3)),
        axis.text = element_text(size = rel(1.3)),
        legend.text = element_text(size = rel(1.3))) # +
  # guides(fill = guide_legend(
  #   override.aes=list(shape = c(21, 22, 24)),
  #   ""),
  #   shape = "none")

ggsave('images/fig_map.png', map_lex, width=2400, height=3000, units="px")
