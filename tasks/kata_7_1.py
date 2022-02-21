"""
https://www.codewars.com/kata/5412509bd436bd33920011bc
https://www.codewars.com/kata/55b051fac50a3292a9000025
https://www.codewars.com/kata/5b180e9fedaa564a7000009a
https://www.codewars.com/kata/5783d8f3202c0e486c001d23
https://www.codewars.com/kata/5864eb8039c5ab9cd400005c
https://www.codewars.com/kata/55d1d6d5955ec6365400006d

"""
# 1
# def maskify(cc):
#     some_str = ''
#     for res in cc[:-4]:
#         some_str += '#'
#     some_str += cc[-4:]
#     return some_str
#
# print(maskify("4556364607935616"))
# print(maskify(     "64607935616"))

# def maskify(cc):
#     return "#"*(len(cc)-4) + cc[-4:]


# 2
# def filter_string(string):
#     some_str = ''
#     for res in string:
#         if res.isdigit():
#             some_str += res
#     return int(some_str)
#
# print(filter_string("011bb2c23c3"))
#
# def filter_string(string):
#     return int(filter(str.isdigit, string))

# # 3
# def solve(s):
#     upper_count = sum(map(str.isupper, s))
#     lower_count = sum(map(str.islower, s))
#     if upper_count > lower_count:
#         return s.upper()
#     else:
#         return s.lower()
#
# print(solve("CODe"))
# print(solve("COde"))
# print(solve("Code"))

#  4
# def to_float_array(arr):
#     res = [float(el) for el in arr]
#     return res

# print(to_float_array(["1.1", "2.2", "3.3"]))

# def to_float_array(arr):
#     return list(map(float, arr))

# def to_float_array(arr):
#     return [float(n) for n in arr]

# 5
# from statistics import median

# def median(array):
#     sor = sorted(array)
#     ln = len(array)
#     index = (ln - 1) // 2

#     if (ln % 2):
#         return sor[index]
#     else:
#         return (sor[index] + sor[index + 1]) / 2

# print(median([33, 99, 100, 30, 29, 50]))
# print(median([3, 50]))
# print(median([1234, 345, 78]))

# 6
# def round_to_next5(n):
#     return n + (-n % 5)

# def round_to_next5(n):
#     return n + ((5 - n) % 5)

# print(round_to_next5(39))
# print(round_to_next5(3))
# print(round_to_next5(-1))
# print(round_to_next5(0))