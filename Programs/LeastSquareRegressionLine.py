# In this challenge, we practice using linear regression techniques

# Task
# A group of five students enrolls in Statistics immediately after taking a Math aptitude test.
# Each student's Math aptitude test score, x, and Statistics course grade, y, can be expressed as the following list of (x,y) points:

# If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics?
# Determine the equation of the best-fit line using the least squares method, then compute and print the value of y when x=80.

# Input Format
# There are five lines of input; each line contains two space-separated integers describing a student's respective maths and statistics grades:

# 95 85
# 85 95
# 80 70
# 70 65
# 60 70

# Output Format
# Print a single line denoting the answer, rounded to a scale of 3 decimal places

x = []
y = []
for i in range(5):
    xi, yi = map(float, input().split())
    x.append(xi)
    y.append(yi)

# summation(xi*yi)
mul_sum = 1
for i in range(5):
    mul_sum += (x[i] * y[i])

xsqr = map(lambda x: x**2, x)
bnum = (5 * mul_sum) - (sum(x) * sum(y))
bden = 5 * sum(xsqr) - (sum(x)**2)

b = bnum / bden
a = sum(y) / len(y) - b * (sum(x) / len(x))

# equation of the line is y= a + bx
y = a + b * 80
print("%.3f" % y)
