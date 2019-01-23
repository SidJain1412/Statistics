# A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized.
# What is the probability that a batch of 10 pistons will contain:

# 1. No more than 2 rejects?
# 2. At least 2 rejects?

# Round both of your answers to a scale of 3 decimal places


tot = 0
nume = 1
# Finding numerator (10 factorial)
for i in range(1, 11):
    nume *= i

# Finding binomial distribution for P(0), 1, 2
for i in range(0, 3):
    den = 1
    val = 1
    # Calculating denominator (refer to binomial dist. formula)
    for j in range(1, i + 1):
        den *= j

    diff = 10 - i
    for j in range(1, diff + 1):
        den *= j

    # 12% probability of pistons not being of correct size
    # Therefore, 88% probability of it being right.
    val = round((nume / den) * (0.12**i) * (0.88**(10 - i)), 4)

    tot += val

# No more than 2 rejects (p0+p1+p2)
print("%.3f" % tot)
# At least 2 rejects (p2+p3+...)
# Therefore it's 1-(<2rejects+ probability of 2 rejects)
print("%.3f" % (1 - tot + val))
