# A random variable follows Poisson distribution with mean of 2.5.
# Find the probability with which the random variable X is equal to 5.

# Input Format

# The first line contains the mean. The second line contains the value we want the probability for:

# 2.5
# 5
# Print output rounded to 3 decimal places

# Declaring variables
num_occurences = 2.5
rand_variable = 5
e = 2.71828

# Calculating denominator factorial
fact = 1
for i in range(2, rand_variable + 1):
    fact *= i

# Using poisson distribution formula
prob = e**(-1 * num_occurences) * (num_occurences**rand_variable) / fact

print("%.3f" % prob)
# Output: 0.067
