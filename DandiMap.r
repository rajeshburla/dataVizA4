
library(ggmap)
library(ggrepel)
library(grid)
library(gridExtra)
library(RCurl)

x <- getURL("https://raw.githubusercontent.com/rajeshburla/dataVizA4/master/mapsNew.csv")
mapdata <- read.csv(text = x)

ggplot(mapData, aes(x = long, y = lat, size=Crowd)) +
  geom_path(lineend = "round")+
  geom_text_repel(data = mapData, aes(x = long, y = lat, label = Place, size=Crowd),
                  color = "#800000", fontface =15) +
  scale_size(range = c(0.5, 10))


dandiRoute <- c(left = 71.280, bottom = 20.2, right = 74.497, top = 23.567)

dandiRoute.map <- get_stamenmap(bbox = dandiRoute, zoom = 7,
                                maptype = "terrain")

dandiRouteGeoSpot <- ggmap(dandiRoute.map) +
  geom_path(data = mapData, aes(x = long, y = lat,size=Crowd), color = "#994d00", lineend = "round")+
  geom_point(data =mapData, aes(x = long, y = lat), color = "#ffff00") +
  geom_text_repel(data = mapData, aes(x = long, y = lat, label = Place), vjust = 1.5, hjust = -0.5,
                  color = "black", fontface =15, size=5)+
  scale_size(range = c(0.8, 15)) + theme(panel.border=element_rect(fill=NA, size = 1))
dandiRouteGeoSpot

