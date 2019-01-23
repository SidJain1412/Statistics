# Given an array of integers, calculate and print the standard deviation
# Your answer should be in decimal form, rounded to 1 decimal place

# Sample Input

# 5
# 10 40 30 50 20
# Sample Output

# 14.1

n = int(input())
numbers = list(map(int, input().split()))

# Finding mean
mean = sum(numbers) / n

# Calculating sum of mean square deviations
msd = 0
for i in numbers:
    msd += (i - mean)**2

# Calculating standard deviation
sd = (msd / n)**0.5
print("%.1f" % sd)
