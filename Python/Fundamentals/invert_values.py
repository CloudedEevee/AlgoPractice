# Change nums in list: positives to negatives and vice versa

# My Code
def invert(lst):
    inv_lst = []
    for num in lst:
        inv_lst.append(-num)
    return inv_lst






# Best Practice

# def invert(lst):
#     return [-x for x in lst]