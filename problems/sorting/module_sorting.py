from functools import cmp_to_key

k = 6
random = [12, 18, 17, 67, 46]


# def compare(i, j):
#     if j % k == i % k:
#         return j < i
#     return j % k < i % k


# print(sorted(random, key=cmp_to_key(compare)))


print(random.sort())
