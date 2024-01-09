# Given an array of nums, count the positives and find the sum of the negatives
# My Code
def count_positives_sum_negatives(arr):
    count_pos = 0
    sum_neg = 0
    for num in arr:
        if num > 0:
            count_pos += 1
        elif num < 0:
            sum_neg += num
        else: continue
    if arr == []:
        return []
    else: return [count_pos, sum_neg]





# Best Practice
# def count_positives_sum_negatives(arr):
#     if not arr: return []
#     pos = 0
#     neg = 0
#     for x in arr:
#         if x > 0:
#             pos += 1
#         if x < 0:
#             neg += x
#     return [pos, neg]