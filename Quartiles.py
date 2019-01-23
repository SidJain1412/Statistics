# Given an array of integers, calculate the respective first quartile (q1), second quartile (q2), and third quartile (q3).
# It is guaranteed that quartiles are integers.


n = int(input())
numbers = list(map(int, input().split()))


numbers = sorted(numbers)


# Function to find median
def median(arr):
    if(len(arr) % 2 != 0):
        return arr[len(arr) // 2]
    else:
        return ((arr[len(arr) // 2] + arr[(len(arr) // 2) - 1]) / 2)


q2 = int(median(numbers))
q1 = int(median(numbers[:len(numbers) // 2]))
# If odd number of elements, median taken from mid+1
if(len(numbers) % 2 == 0):
    q3 = int(median(numbers[(len(numbers) // 2):]))
else:
    q3 = int(median(numbers[(len(numbers) // 2) + 1:]))


print(q1)
print(q2)
print(q3)
