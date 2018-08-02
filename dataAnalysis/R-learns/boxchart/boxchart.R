# boxplot(x, data, notch, varwidth, names, main)


# mpg（英里/加仑）和cyl（气缸数）
input <- mtcars[,c('mpg','cyl')]
print(head(input))




# Give the chart file a name.
png(file = "E:/R-learns/boxchart/boxplot.png")

# Plot the chart.
boxplot(mpg ~ cyl, data = mtcars, xlab = "Number of Cylinders",
   ylab = "Miles Per Gallon", main = "Mileage Data")

# Save the file.
dev.off()






# Give the chart file a name.
png(file = "E:/R-learns/boxchart/boxplot_with_notch.png")

# Plot the chart.
boxplot(mpg ~ cyl, data = mtcars, 
   xlab = "Number of Cylinders",
   ylab = "Miles Per Gallon", 
   main = "Mileage Data",
   notch = TRUE, 
   varwidth = TRUE, 
   col = c("green","yellow","purple"),
   names = c("High","Medium","Low")
)
# Save the file.
dev.off()













