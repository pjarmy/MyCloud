# Create a sequence of numbers from 32 to 44.
print(seq(32,44))

# Find mean of numbers from 25 rto 82.
print(mead(25,82))

# Find sum of numbers from 41 ro 68.
print (sum(41:68))




# Create a function to print squares of numbers in sequence.
new.function <- function(a) {
	for (i in 1:a) {
		b <- i^2
		print(b)
	}
}

# Call the function new.function supplying 6 as an argment.
new.function(6)


# Create a function to print squares of numbers in sequence.
new.function <- function() {
	for (i in 1:5) {
		print(i^2)
	}
}

# Call the function without supplying an argument.
new.function


# Create a function with arguments
new.function <- function(a,b,c) {
	result <- a * b +c
	print(result)
}

# Call the function by position of arguments.
new.function(5,3,11)

# call the function by names of the arguments.
new.function(a = 11 , b = 5 , c = 3)


# Create a function with arguments.
new.function <- function(a,b) {
	print(a^2)
	print(a)
	print(b)
}

# Evaluate the function without supplying one of the arguments.
new.function(6)









