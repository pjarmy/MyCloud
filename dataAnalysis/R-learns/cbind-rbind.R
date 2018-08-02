# Create vector objects.
city <- c("Tampa", "Seattle", "Hartford", "Denver")
state <- c("FL", "WA", "CT", "CO")
zipcode <- c(33602,98104,06161,80294)

# Combine above three vectors into one data frame.
address <- cbind(city,state,zipcode)

# Print a header
cat("# # # # The First data frame")

# Print the data frame
print(address)

# Create another data frame with similar columns.
new.address <- data.frame(
    city = c("Lowry", "Charlotte"),
    state = c("CO", "FL"),
    zipcode = c("80230", "33949"),
    stringsAsFactors = FALSE
)

# Print a header.
cat("# # # The Second data frame")

# Print the data frame.
print(new.address)

# Combine rows form both the data frame.
all.address <- rbind(address, new.address)

# Print a header.
cat("# # # The combined data frame")

# Print the result.
print(all.address)









