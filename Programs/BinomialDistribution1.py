# The ratio of boys to girls for babies born in Russia is 1.09:1
# What proportion of Russian families with exactly 6 children will have at least 3 boys?

# Write a program to compute the answer using the above parameters.
# Then print your result, rounded to a scale of 3 decimal places
# Assume input as 1.09:1, or hardcode


tot = 0
# probability of child being a boy
pboy = 1.09 / 2.09
# probability of child being a girl
pgirl = 1 / 2.09
# numerator for binomial distribution
# Refer formula for binomial distribution
nume = 6 * 5 * 4 * 3 * 2 * 1  # 6 factorial

# calculating sum of distributions (at LEAST 3 boys)
for i in range(3, 7):
    # denominator
    den = 1
    # value of the current distribution
    val = 1
    for j in range(1, i + 1):
        den *= j

    diff = 6 - i
    for j in range(1, diff + 1):
        den *= j
    # calculating final distribution result for i
    val = round((nume / den) * (pboy**i) * (pgirl**(6 - i)), 4)
    # summing it all
    tot += val

print("%.3f" % tot)
# Output: 0.696
