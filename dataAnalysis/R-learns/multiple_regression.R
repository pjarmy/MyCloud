# 数据集“mtcars”。 它给出了每加仑里程（mpg），气缸排量（“disp”），
# 马力（“hp”），汽车重量（“wt”）

input <- mtcars[,c("mpg","disp","hp","wt")]
print(head(input))



input <- mtcars[,c("mpg","disp","hp","wt")]

# Create the relationship model.
model <- lm(mpg~disp+hp+wt, data = input)

# Show the model.
print(model)

# Get the Intercept and coefficients as vector elements.
cat("# # # # The Coefficient Values # # # ","
")

a <- coef(model)[1]
print(a)

Xdisp <- coef(model)[2]
Xhp <- coef(model)[3]
Xwt <- coef(model)[4]

print(Xdisp)
print(Xhp)
print(Xwt)


# 基于上述截距和系数值，我们创建了数学方程。
# Y = a+Xdisp.x1+Xhp.x2+Xwt.x3
# or
# Y = 37.15+(-0.000937)*x1+(-0.0311)*x2+(-3.8008)*x3


# 应用方程预测新值
# 当提供一组新的位移，马力和重量值时，我们可以使用上面创建的回归方程来预测里程数。
# 对于disp = 221，hp = 102和wt = 2.91的汽车，预测里程为 -
# Y = 37.15+(-0.000937)*221+(-0.0311)*102+(-3.8008)*2.91 = 22.7104




