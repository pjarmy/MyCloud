# pie(x, labels, radius, main, col, clockwise)

# Create data for the graph.
x <- c(21, 62, 10, 53)
labels <- c("London", "New York", "Singapore", "Mumbai")

# Give the chart file a name.
png(file = "E:/R-learns/pie/city.jpg")

# Plot the chart.
pie(x,labels)

# Save the file.
dev.off()



# Create data for the graph.
x <- c(21, 62, 10, 53)
labels <- c("London", "New York", "Singapore", "Mumbai")

# Give the chart file a name.
png(file = "E:/R-learns/pie/city_title_colours.jpg")

# Plot the chart with title and rainbow color pallet.
pie(x, labels, main = "City pie chart", col = rainbow(length(x)))

# Save the file.
dev.off()



# piepercent ±ý×´Í¼°Ù·Ö±È
# Create data for the graph.
x <-  c(21, 62, 10,53)
labels <-  c("London","New York","Singapore","Mumbai")

piepercent<- round(100*x/sum(x), 1)

# Give the chart file a name.
png(file = "E:/R-learns/pie/city_percentage_legends.jpg")

# Plot the chart.
pie(x, labels = piepercent, main = "City pie chart",col = rainbow(length(x)))
legend("topright", c("London","New York","Singapore","Mumbai"), cex = 0.8,
   fill = rainbow(length(x)))

# Save the file.
dev.off()




# 3D±ýÍ¼ pie3D    install.packages(¡°plotrix¡±)
# Get the library.
library(plotrix)

# Create data for the graph.
x <-  c(21, 62, 10,53)
lbl <-  c("London","New York","Singapore","Mumbai")

# Give the chart file a name.
png(file = "E:/R-learns/pie/3d_pie_chart.jpg")

# Plot the chart.
pie3D(x,labels = lbl,explode = 0.1, main = "Pie Chart of Countries ")

# Save the file.
dev.off()



# ÉÈÐÎÍ¼ fan plot
png(file = "E:/R-learns/pie/fan_plot_chart.jpg")

fan.plot(x, labels = lbl, main = "Fan Plot", col = terrain.colors(length(x)))

legend("topright", lbl, cex = 0.8, fill = terrain.colors(length(x)))


