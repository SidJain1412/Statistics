# Given two n-element data sets, X and Y, calculate the value of the Pearson correlation coefficient.

# Input Format
# The first line contains an integer, n, denoting the size of data sets X and Y. 
# The second line contains n space-separated real numbers (scaled to at most one decimal place), defining data set X. 
# The third line contains n space-separated real numbers (scaled to at most one decimal place), defining data set Y.

# Sample Input
# 10
# 10 9.8 8 7.8 7.7 7 6 5 4 2
# 200 44 32 24 22 17 15 12 8 4

# Sample Output
# 0.612

# A Pearson correlation is a number between -1 and 1 that indicates the extent to which two variables are linearly related.
# The Pearson correlation is also known as the “product moment correlation coefficient” (PMCC) or simply “correlation”.

size = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

meanx = sum(x) / size
meany = sum(y) / size


def find_stddev(data, mean):
    stddev = 0
    for i in data:
        stddev += (i - mean) ** 2
    return (stddev / len(data)) ** 0.5


stddev_x = find_stddev(x, meanx)
stddev_y = find_stddev(y, meany)

pearson = 0
for i in range(size):
    pearson += (x[i] - meanx) * (y[i] - meany)

pearson = pearson / (size * stddev_x * stddev_y)

print("%.3f" % pearson)
