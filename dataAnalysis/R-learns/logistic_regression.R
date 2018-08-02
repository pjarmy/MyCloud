# 在“mtcars”数据集中，传输模式（自动或手动）由am列描述，它是一个二进制值（0或1）。 
# 我们可以在列“am”和其他3列（hp，wt和cyl）之间创建逻辑回归模型。

# Select some columns form mtcars.
input <- mtcars[,c("am","cyl","hp","wt")]

print(head(input))



input <- mtcars[,c("am","cyl","hp","wt")]

am.data = glm(formula = am ~ cyl + hp + wt, data = input, family = binomial)

print(summary(am.data))


# 在总结中，对于变量“cyl”和“hp”，最后一列中的p值大于0.05，我们认为它们对变量“am”的值有贡献是无关紧要的。 只有重量（wt）影响该回归模型中的“am”值。