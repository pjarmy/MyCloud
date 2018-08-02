install.packages("randomForest)

# randomForest(formula, data)


# Load the party package. It will automatically load other required packages.
library(party)

# Print some records from data set readingSkills.
print(head(readingSkills))



# Load the party package. It will automatically load other required packages.
library(party)
library(randomForest)

# Create the forest.
output.forest <- randomForest(nativeSpeaker ~ age + shoeSize + score, 
           data = readingSkills)

# View the forest results.
print(output.forest) 

# Importance of each predictor.
print(importance(fit,type = 2)) 


