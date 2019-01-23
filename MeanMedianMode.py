# Sample Input

# 10
# 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

# Sample Output

# 43900.6
# 44627.5
# 4978

num = int(input("Number of elements: "))
data = list(map(int, (input("Enter elements separated by spaces: ").split(' '))))
print()

# MEAN:
print("Mean: ", sum(data) / num)


# MEDIAN:
# sorting the list
data = sorted(data)

if(num % 2 == 0):
    # If even number of elements, median is average of the middle elements
    median = (data[(num // 2) - 1] + data[(num // 2)]) / 2
else:
    # Odd number of elements, median is middle element
    median = data[len(data) // 2]
print("Median: ", median)

# MODE:
numbers = {}

# finding count of each value in the list
for item in data:
    if item not in numbers:
        numbers[item] = 1
    else:
        numbers[item] = numbers[item] + 1


# Finding most repeated element
max_count = 0

for key in numbers:
    if numbers[key] > max_count:
        max_count = numbers[key]

# If there are more than one elements repeated highest number of times
# We show the least one of those
max_modal_elements = []

for key in numbers:
    if numbers[key] == max_count:
        max_modal_elements.append(key)

mode = min(max_modal_elements)
print("Mode: ", mode)
