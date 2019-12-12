## load pckg
listofpackages <- c("kohonen","dplyr","ggplot2","ggforce","ggrepel")
# ggforce : 4 geom_circle function
# ggrepel : 4 geom_text_repel
newpackages <- listofpackages[!(listofpackages %in% installed.packages()[,"Package"])]
if(length(newpackages)) install.packages(newpackages,repos='http://cran.us.r-project.org')
for(i in 1:length(listofpackages)) library(listofpackages[i],character.only=T)

somplot<-function(hh,gridxdim,gridydim,somsd=0.1,label=1:dim(hh)[1]){
set.seed(777)
#library(kohonen)
somrslt <- som(hh, somgrid(gridxdim,gridydim,"hexagonal"))
#library(dplyr)
somgrd <- somrslt[[4]]$pts %>%
  as_tibble %>% 
  mutate(id=row_number())

sompts <- tibble(id = somrslt[[2]],
                  dist = somrslt[[3]])
sompts <- sompts %>% left_join(somgrd,by="id")
sompts$x<-sompts$x+rnorm(dim(hh)[1])*somsd
sompts$y<-sompts$y+rnorm(dim(hh)[1])*somsd
ndist <- unit.distances(somrslt$grid)
cddist <- as.matrix(object.distances(somrslt, type = "codes"))
cddist[abs(ndist - 1) > .001] <- NA
neigh.dists <- colMeans(cddist, na.rm = TRUE)
somgrd <- somgrd %>% mutate(dist=neigh.dists)
#library(ggplot2)
#library(ggforce) # for geom_circle function
#library(ggrepel) # for geom_text_repel
p <- somgrd %>% 
     ggplot(aes(x0=x,y0=y))+ggforce::geom_circle(aes(r=0.5,fill=dist))+
     scale_fill_gradient(low="white",high="gray25",name="Distance")+
     theme(panel.background = element_blank(),
           axis.ticks = element_blank(),
           panel.grid = element_blank(),
           axis.text = element_blank(),
           axis.title = element_blank(),
           legend.position = "right")+
           geom_point(data = sompts,aes(x,y),alpha = 0.8,cex=3)+
           geom_text_repel(data=sompts,aes(x,y,label=vname),cex=3)
p
}
