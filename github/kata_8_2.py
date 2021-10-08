"""
https://www.codewars.com/kata/523b4ff7adca849afe000035
https://www.codewars.com/kata/523b623152af8a30c6000027
https://www.codewars.com/kata/5625618b1fe21ab49f00001f
https://www.codewars.com/kata/5acc3634c6fde760ec0001f7
https://www.codewars.com/kata/57f5e7bd60d0a0cfd900032d

"""

# 1
# def greet():
#     return "hello world!"

# 2
# def square(n):
#     return n ** 2

# 3
# def say_hello(name):
#     return f"Hello, {name}"

# 4
# def solve(nums, div):
#     res = [el1 % div + el1 for el1 in nums]
#     return res
#
# print(solve([2, 7, 5, 9, 100, 34, 32, 0], 3))

# nums = [2, 7, 5, 9, 100, 34, 32, 0], div = 3
#   ==>  [4, 8, 7, 9, 101, 35, 34, 0]

# def solve(nums,div):
#     return [x + x % div for x in nums]

# 5
# def missing_no(nums):
#     n = len(list(nums))
#     res = (n + 1) * (n + 2) / 2
#     sum_nums = sum(nums)
#     return res - sum_nums
# #
# def examples():
#     nums = list(range(0,11))
#     nums.remove(5)
#     return nums
#
# miss = examples()
# # res = missing_no(5)
# # print(res)
# print(miss)
# print(missing_no(miss))
