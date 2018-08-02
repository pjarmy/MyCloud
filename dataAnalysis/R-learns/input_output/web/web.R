install.packages("RCurl")
install.packages("XML")
install.packages("stringr")
install.packages("plyr")

library("Rcurl")
library("XML")
library("stringr")
library("plyr")


setwd("E:/R-learns/input_output/web")


# Read the URL.
url <- "https://www.geos.ed.ac.uk/~weather/jcmb_ws/"

# Gather the html links present in the webpage.
links <- getHTMLLinks(url)

# Identify only the links which point to the JCMB 2015 files. 
filenames <- links[str_detect(links, "JCMB_2015")]

# Store the file names as a list.
filenames_list <- as.list(filenames)

# Create a function to download the files by passing the URL and filename list.
downloadcsv <- function (mainurl,filename) {
   filedetails <- str_c(mainurl,filename)
   download.file(filedetails,filename)
}

# Now apply the l_ply function and save the files into the current R working directory.
l_ply(filenames,downloadcsv,mainurl = "https://www.geos.ed.ac.uk/~weather/jcmb_ws/")



