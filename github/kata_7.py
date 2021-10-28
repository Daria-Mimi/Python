""""
https://www.codewars.com/kata/56684677dc75e3de2500002b
https://www.codewars.com/kata/588f5a38ec641b411200005b
https://www.codewars.com/kata/57ee99a16c8df7b02d00045f
https://www.codewars.com/kata/5949481f86420f59480000e7
https://www.codewars.com/kata/59a8570b570190d313000037
https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763


"""
# 1
# Left = 'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'
# Right = ('y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm')
# def comfortable_word(word):
#     some_str = ""
#     for some_str in Left:
#         # res += res
#         if word == some_str:
#             return print(True)
#         else:
#             return print(False)
#     for res1 in Right:
#         if word == res1:
#             return print(True)
#         else:
#             return print(False)
#
#
# print(comfortable_word("yams"))

# def comfortable_word(word):
#     el = list(word)
#     if el in Left:
#         return print(True)
#     else:
#         return print(False)
#
#
# print(comfortable_word("yams"))


# right = ['y', 'u', 'i', 'o', 'p', 'h', 'j','k', 'l', 'n', 'm']
# left = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
# arr = []
#
# def comfortable_word(word):
#     for arr in word:
#         if arr == right == left:
#             return True
#     return False
#
#
# print(comfortable_word("yams"))

# 2
# def how_many_years(date1, date2):
#     date1 = int(date1[0:4])
#     date2 = int(date2[0:4])
#     if date1 <= date2:
#         return date2 - date1
#     if date1 >= date2:
#         return date1 - date2
#
# print(how_many_years('1997/10/10', '2015/10/10'))
#
# def how_many_years (date1,date2):
#     return abs(int(date1[:4]) - int(date2[:4]))

# 3
# def flatten_and_sort(array):
#     new_array = []
#     for arr in array:
#         for el in arr:
#             new_array.append(el)
#     return sorted(new_array)

# def flatten_and_sort(array):
#     return sorted([j for i in array for j in i])
#
# print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))
# print(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6], [1, 2, 3, 4, 5, 6, 100]]))

# 4
# def odd_or_even(arr):
#     res = sum(arr)
#     if res % 2 or 0:
#         return "odd"
#     else:
#         return "even"

# def odd_or_even(arr):
#     return 'even' if sum(arr) % 2 == 0 else 'odd'
#
# print(odd_or_even([0, 1, 2]))
# print(odd_or_even([0, 1, 3]))
# print(odd_or_even([1023, 1, 2]))

# 5
# def sum_cubes(n):
#     total = 0
#     while n > 0:
#         total += n ** 3
#         n -= 1
#     return total

# def sum_cubes(n):
#     return sum(el ** 3 for el in range(0, n + 1))

# print(sum_cubes(123))

# 6
# def show_sequence(n):
#     res = range(0, n + 1)
#     new_array = []
#     for arr in res:
#         new_array.append(arr)
#     return sum(new_array)
#
# print(show_sequence(6))

# n = 6
# res = list(range(0, n + 1))
# print(sum(res))