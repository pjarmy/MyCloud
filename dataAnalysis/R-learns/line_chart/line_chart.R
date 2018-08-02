# plot(v,type,col,xlab,ylab)

# Create the data for the chart.
v <- c(7,12,28,3,41)

# Give the chart file a name.
png(file = "E:/R-learns/line_chart/line_chart.jpg")

# Plot the bar chart. 
plot(v,type = "o")

# Save the file.
dev.off()





# Create the data for the chart.
v <- c(7,12,28,3,41)

# Give the chart file a name.
png(file = "E:/R-learns/line_chart/line_chart_label_colored.jpg")

# Plot the bar chart.
plot(v,type = "o", col = "red", xlab = "Month", ylab = "Rain fall",
   main = "Rain fall chart")

# Save the file.
dev.off()






# Create the data for the chart.
v <- c(7,12,28,3,41)
t <- c(14,7,6,19,3)
r <- c("BeiJing", "ShangHai")

# Give the chart file a name.
png(file = "E:/R-learns/line_chart/line_chart_2_lines.jpg")

# Plot the bar chart.
plot(v,type = "o",col = "red", xlab = "Month", ylab = "Rain fall", 
   main = "Rain fall chart")

lines(t, type = "o", col = "blue")

legend("topleft", r, cex = 1.3, fill = c("red","blue"))

# Save the file.
dev.off()




