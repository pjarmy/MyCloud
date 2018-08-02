# plot(x, y, main, xlab, ylab, xlim, ylim, axes)
# wt（重量）和mpg（英里/加仑）

input <- mtcars[,c('wt','mpg')]
print(head(input))


# Get the input values.
input <- mtcars[,c('wt','mpg')]

# Give the chart file a name.
png(file = "E:/R-learns/scatterplot/scatterplot.png")

# Plot the chart for cars with weight between 2.5 to 5 and mileage between 15 and 30.
plot(x = input$wt,y = input$mpg,
   xlab = "Weight",
   ylab = "Milage",
   xlim = c(2.5,5),
   ylim = c(15,30),		 
   main = "Weight vs Milage"
)
	 
# Save the file.
dev.off()





### pairs(formula, data)

# Give the chart file a name.
png(file = "E:/R-learns/scatterplot/scatterplot_matrices.png")

# Plot the matrices between 4 variables giving 12 plots.

# One variable with 3 others and total 4 variables.

pairs(~wt+mpg+disp+cyl,data = mtcars,
   main = "Scatterplot Matrix")

# Save the file.
dev.off()






