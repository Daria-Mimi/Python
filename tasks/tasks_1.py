# def anagrams(word, words):
#     if sorted(word) == sorted(words):
#         return True
#     else:
#         return False
#
# print(anagrams("abc", "cba"))


'''
https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e
https://www.codewars.com/kata/545af3d185166a3dec001190
https://www.codewars.com/kata/544675c6f971f7399a000e79
https://www.codewars.com/kata/57f24e6a18e9fad8eb000296
https://www.codewars.com/kata/53ee5429ba190077850011d4
https://www.codewars.com/kata/5713bc89c82eff33c60009f7
'''

# 1
# def sum_of_differences(arr):
#     return max(arr) - min(arr) if arr else 0


# print(sum_of_differences([-3, -2, -1]))
# print(sum_of_differences([1, 1, 1, 1, 1]))
# print(sum_of_differences([-17, 17]))
# print(sum_of_differences([]))
# print(sum_of_differences([1, 2, 10]))


# 2
# def each_cons(lst, n):
#     arr = []
#     for i in range(len(lst)):
#         if len(lst[i:i + n]) == n:
#             arr.append(lst[i:i + n])
#     return arr

# print(each_cons([3, 5, 8, 13], 1))
# print(each_cons([3, 5, 8, 13], 2))
# print(each_cons([3, 5, 8, 13, 15, 18, 20, 19, 3, 5], 3))
# print(each_cons([], 3))


# 3
# def string_to_number(s):
#     return int(s)
#
# print(string_to_number("1234"))
# print(string_to_number("605"))
# print(string_to_number("1405"))
# print(string_to_number("-7"))


# 4
# words = {1: "I love you",
#        2: "a little",
#        3: "a lot",
#        4: "passionately",
#        5: "madly",
#        0: "not at all"
# }

# def how_much_i_love_you(nb_petals):
#        return words.get(nb_petals % 6)

# print(how_much_i_love_you(7))
# print(how_much_i_love_you(3))
# print(how_much_i_love_you(6))


# 5
# def double_integer(i):
#        return i * 2


# 6
# def to_freud(sentence):
#        return ' '.join('sex' for _ in sentence.split())

# print(to_freud("test"))
# print(to_freud("sexy sex"))
# print(to_freud("This is a test"))