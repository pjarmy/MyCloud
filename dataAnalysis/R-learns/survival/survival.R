install.packages("survival")


Surv(time,event)
survfit(formula)


# Load the library.
library("survival")

# Print first few rows.
print(head(pbc))


# Load the library.
library("survival")

# Create the survival object. 
survfit(Surv(pbc$time,pbc$status == 2)~1)

# Give the chart file a name.
png(file = "E:/R-learns/survival/survival.png")

# Plot the graph. 
plot(survfit(Surv(pbc$time,pbc$status == 2)~1))

# Save the file.
dev.off()


