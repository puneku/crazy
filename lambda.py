from functools import reduce
nums = [3, 1, 8, 4, 6, 0, 9, 2, 5, 7]

print(nums)

odds = list(filter(lambda a: a % 2 != 0, nums))

print(odds)

# Adding 5 to each element

addon = list(map(lambda a: a+5, odds))

print(addon)

avg = reduce(lambda a,b: a+b, addon)/len(addon)

print('average of addon is {}'.format(avg))