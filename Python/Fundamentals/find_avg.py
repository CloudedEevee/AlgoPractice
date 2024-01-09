# Write a function which calculates the average of the numbers in a given list.

# My Code:
def find_average(numbers):
    return (sum(numbers) / len(numbers) if len(numbers) else 0)

# Best Practice:
# def find_average(array):
#     return sum(array) / len(array) if array else 0