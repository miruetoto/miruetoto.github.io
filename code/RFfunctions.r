## load pckg
listofpackages <- c("ADMM")
newpackages <- listofpackages[!(listofpackages %in% installed.packages()[,"Package"])]
if(length(newpackages)) install.packages(newpackages,repos='http://cran.us.r-project.org')
library(listofpackages)
