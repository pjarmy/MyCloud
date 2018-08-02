install.packages("xlsx")

# Verify the package is installed.
any(grepl("xlsx",installed.packages()))

# Load the library into R workspace.
library("xlsx")

Sys.setenv(JAVA_HOME='C:/Program Files/Java/jre1.8.0_171')
# java -verbose windows查看java存放路径


setwd("E:/R-learns/input_output/xlsx")

# Read the first worksheet in the file input.xlsx.
data <- read.xlsx("input.xlsx", sheetIndex = 1)
print(data)


# Read the first worksheet in the file input.xlsx.
data <- read.xlsx("input.xlsx", sheetIndex = 2)
print(data)