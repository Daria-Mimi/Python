"""
https://www.codewars.com/kata/598f76a44f613e0e0b000026
https://www.codewars.com/kata/5b39e91ee7a2c103300018b3
https://www.codewars.com/kata/56676e8fabd2d1ff3000000c
https://www.codewars.com/kata/5a00e05cc374cb34d100000d

"""
# 1
# import re
# def sum_of_integers_in_string(s):
#     sum = 0
#     y = re.findall('\d+', s)
#     for el in range(len(y)):
#         sum += int(y[el])
#     return print(sum)
#
# sum_of_integers_in_string("12.4")
# sum_of_integers_in_string("h3ll0w0rld")
# sum_of_integers_in_string("The Great Depression lasted from 1929 to 1939.")
# sum_of_integers_in_string("C4t5 are 4m4z1ng.")
#
# import re
# def sum_of_integers_in_string(s):
#     return sum(int(x) for x in re.findall(r"(\d+)", s))
#
# import re
# def sum_of_integers_in_string(s):
#     return sum(map(int, re.findall("\d+", s)))
#
# import re
# def sum_of_integers_in_string(s):
#   return sum(int(i) for i in re.findall('\d+', s))

# 2
# def remove_consecutive_duplicates(s):
#     l = []
#     for word in s.split():
#         if word not in l:
#             l.append(word)
#     return print(" ".join(l))

# def remove_consecutive_duplicates(s):
#     return print(" ".join(sorted(set(s.split()), key=s.index)))
#
# remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta')

# 3
# def find_needle(haystack):
#     count = 0
#     for el in haystack:
#         if el == 'needle':
#             return print(f'found the needle at position {count}')
#         else:
#             count += 1
#             continue
#
# find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])
# find_needle(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago'])
# find_needle([1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 5, 4, 3, 4, 5, 6, 67, 5, 5, 3, 3, 4, 2, 34, 234, 23, 4, 234, 324, 324, 'needle', 1, 2, 3, 4, 5, 5, 6, 5, 4, 32, 3, 45, 54])

# def find_needle(haystack):
#     return 'found the needle at position {}'.format(haystack.index('needle'))

# def find_needle(haystack):
#     return f'found the needle at position {haystack.index("needle")}'

# 4
# def reverse_seq(n):
#     res = []
#     for el in range(1, n + 1):
#         res.append(el)
#     res.reverse()
#     return print(res)
#
#
# reverse_seq(5)
# reverse_seq(8)
# reverse_seq(3)
#
# def reverseseq(n):
#     return list(range(n, 0, -1))
#
# def reverseseq(n):
#     return [x for x in range(n,0,-1)]

