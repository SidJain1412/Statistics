# The first line contains an integer, N , denoting the number of elements in arrays X and W.
# The second line contains N space-separated integers describing the respective elements of array X.
# The third line contains W space-separated integers describing the respective elements of array W.
# Print the weighted mean on a new line. Your answer should be rounded to a scale of 1 decimal place.

# Sample Input

# 5
# 10 40 30 50 20
# 1 2 3 4 5
# Sample Output

# 32.0


n = int(input())
numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))
tot = 0
for i in range(n):
    tot += numbers[i] * weights[i]

print("%.1f" % (tot / sum(weights)))
