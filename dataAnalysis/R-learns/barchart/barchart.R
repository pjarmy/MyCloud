#barplot(H, xlab, ylab, main, names.arg, col)

# Create the data for the chart.
H <- c(7,12,28,3,41)

# Give the chart file a name and save it.
png(file = "E:/R-learns/barchart/barchart.png")

# Plot the bar chart.
barplot(H)

# Save the file.
dev.off()




# Create the data for the chart.
H <- c(7,12,28,3,41)
M <- c("Mar","Apr","May","Jun","Jul")

# Give the chart file a name.
png(file = "E:/R-learns/barchart/barchart_months_revenue.png")

# Plot the bar chart.
barplot(H,names.arg = M,xlab = "Month",ylab = "Revenue",col = "blue",
main = "Revenue chart",border = "red")

# Save the file.
dev.off()





# Create the input vectors.
colors <- c("green","orange","brown")
months <- c("Mar","Apr","May","Jun","Jul")
regions <- c("East","West","North")

# Create the matrix of the values.
Values <- matrix(c(2,9,3,11,9,4,8,7,3,12,5,2,8,10,11),nrow = 3,ncol = 5,byrow = TRUE)

# Give the chart file a name.
png(file = "E:/R-learns/barchart/barchart_stacked.png")

# Create the bar chart.
barplot(Values,main = "total revenue",names.arg = months,xlab = "month",ylab = "revenue",
   col = colors)

# Add the legend to the chart.
legend("topleft", regions, cex = 1.3, fill = colors)

# Save the file.
dev.off()













