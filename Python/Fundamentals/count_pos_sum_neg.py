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