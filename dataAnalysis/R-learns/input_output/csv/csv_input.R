# Get and print current working directory.
print(getwd())

# Set current working directory.
setwd("E:/R-learns/input_output/csv")

# Get and print current working directory.
print(getwd())


#input.csv
#id,name,salary,start_date,dept
#1,Rick,623.3,2012-01-01,IT
#2,Dan,515.2,2013-09-23,Operations
#3,Michelle,611,2014-11-15,IT
#4,Ryan,729,2014-05-11,HR
# ,Gary,843.25,2015-03-27,Finance
#6,Nina,578,2013-05-21,IT
#7,Simon,632.8,2013-07-30,Operations
#8,Guru,722.5,2014-06-17,Finance



data <- read.csv("input.csv")
print(data)


data <- read.csv("input.csv")
print(is.data.frame(data))
print(ncol(data))
print(nrow(data))



# 获得最高工资
# Create a data frame.
data <- read.csv("input.csv")

# Get the max salary from data frame.
sal <- max(data$salary)
print(sal)




# 获取具有最高工资的人的详细信息
# Create a data frame.
data <- read.csv("input.csv")

# Get the max salary from data frame.
sal <- max(data$salary)

# Get the person detail having max salary.
retval <- subset(data, salary == max(salary))
print(retval)



# 获取所有的IT部门员工的信息
# Create a data frame.
data <- read.csv("input.csv")

retval <- subset( data, dept == "IT")
print(retval)



# 获得工资大于600的IT部门的人员
# Create a data frame.
data <- read.csv("input.csv")

info <- subset(data, salary > 600 & dept == "IT")
print(info)




# 获得2014年或之后加入的人
# Create a data frame.
data <- read.csv("input.csv")

retval <- subset(data, as.Date(start_date) > as.Date("2014-01-01"))
print(retval)



# 写入CSV文件    write.csv()

# Create a data frame.
data <- read.csv("input.csv")
retval <- subset(data, as.Date(start_date) > as.Date("2014-01-01"))

# Write filtered data into a new file.
write.csv(retval,"output.csv")
newdata <- read.csv("output.csv")
print(newdata)










