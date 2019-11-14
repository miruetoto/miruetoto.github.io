## load pckg
listofpackages <- c("ADMM")
# ggforce : 4 geom_circle function
# ggrepel : 4 geom_text_repel
newpackages <- listofpackages[!(listofpackages %in% installed.packages()[,"Package"])]
if(length(newpackages)) install.packages(newpackages)
library(listofpackages)
