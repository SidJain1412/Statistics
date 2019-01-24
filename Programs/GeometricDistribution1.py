# The probability that a machine produces a defective product is 1/3.
# What's the probability that the 1st defect is found on the 5th inspection?

# Input Format

# The first line contains the respective space-separated numerator and denominator for the probability of a defect,
# and the second line contains the inspection we want the probability of being the first defect for:

# 1 3
# 5
# Output rounded off to 3 decimal places

nume, den = map(int, input().split())
# probability (numerator/denominator)
prob = nume / den
# inspection number
numins = int(input())

# Refer to formula for geometric distribution
op = prob * (1 - prob)**(numins - 1)

print("%.3f" % op)
