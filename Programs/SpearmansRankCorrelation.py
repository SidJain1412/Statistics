# Task
# Given two n-element data sets, X and Y, calculate the value of Spearman's rank correlation coefficient.

# Input Format

# The first line contains an integer, n, denoting the number of values in data sets X and Y. 
# The second line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set X. 
# The third line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set Y.

# Sample Input
# 10
# 10 9.8 8 7.8 7.7 1.7 6 5 1.4 2
# 200 44 32 24 22 17 15 12 8 4

# Sample Output
# 0.903
# Table: https://s3.amazonaws.com/hr-challenge-images/21707/1463946457-87c79bda5e-Screenshot2016-05-2301.16.57.png
# Formula: https://www.onlinemath4all.com/images/spearmancorrelation1.png

size = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

sx = sorted(x)
sy = sorted(y)

rank_x = []
rank_y = []

for i in range(size):
    # sx.index finds position of element x[i] in sx
    rank_x.append(sx.index(x[i]) + 1)
    rank_y.append(sy.index(y[i]) + 1)

di_sqr = []
for i in range(size):
    di_sqr.append((rank_x[i] - rank_y[i])**2)

sum_di = sum(di_sqr)

den = size * (size**2 - 1)
num = 6 * sum_di
rxy = 1 - (num / den)

print("%.3f" % rxy)
