# 标准分布  正态分布

# dnorm(x, mean, sd)
# pnorm(x, mean, sd)
# qnorm(p, mean, sd)
# rnorm(n, mean, sd)

# dnorm（）
# 该函数给出给定平均值和标准偏差在每个点的概率分布的高度。

# Create a sequence of numbers between -10 and 10 incrementing by 0.1.
x <- seq(-10, 10, by = .1)

# Choose the mean as 2.5 and standard deviation as 0.5.
y <- dnorm(x, mean = 2.5, sd = 0.5)

# Give the chart file a name.
png(file = "E:/R-learns/std.deviation/dnorm.png")

plot(x,y)

# Save the file.
dev.off()





# pnorm（）
# 该函数给出正态分布随机数的概率小于给定数的值。 它也被称为“累积分布函数”。

# Create a sequence of numbers between -10 and 10 incrementing by 0.2.
x <- seq(-10,10,by = .2)
 
# Choose the mean as 2.5 and standard deviation as 2. 
y <- pnorm(x, mean = 2.5, sd = 2)

# Give the chart file a name.
png(file = "E:/R-learns/std.deviation/pnorm.png")

# Plot the graph.
plot(x,y)

# Save the file.
dev.off()





# qnorm（）
# 该函数采用概率值，并给出累积值与概率值匹配的数字。

# Create a sequence of probability values incrementing by 0.02.
x <- seq(0, 1, by = 0.02)

# Choose the mean as 2 and standard deviation as 3.
y <- qnorm(x, mean = 2, sd = 1)

# Give the chart file a name.
png(file = "E:/R-learns/std.deviation/qnorm.png")

# Plot the graph.
plot(x,y)

# Save the file.
dev.off()




# RNORM（）
# 此函数用于生成分布正常的随机数。 它将样本大小作为输入，并生成许多随机数。 我们绘制一个直方图来显示生成的数字的分布。
# Create a sample of 50 numbers which are normally distributed.
y <- rnorm(50)

# Give the chart file a name.
png(file = "E:/R-learns/std.deviation/rnorm.png")

# Plot the histogram for this sample.
hist(y, main = "Normal DIstribution")

# Save the file.
dev.off()