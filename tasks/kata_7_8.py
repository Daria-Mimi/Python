"""
https://www.codewars.com/kata/5bb0c58f484fcd170700063d
https://www.codewars.com/kata/56747fd5cb988479af000028
https://www.codewars.com/kata/573d498eb90ccf20a000002a


"""
# 1
# def pillars(num_pill, dist, width):
#     return print((num_pill - 1) * dist * 100 + max(num_pill - 2, 0) * width)

# def pillars(num_pill, dist, width):
#     if num_pill <= 1:
#         return 0
#     else:
#         return (num_pill - 2) * width + (num_pill - 1) * dist * 100

# pillars(1, 10, 10) #0
# print(pillars(2, 20, 25)) #2000
# print(pillars(11, 15, 30)) #15270

# 2
# def get_middle(s):
#     if (len(s) % 2 == 0):
#         return "" + s[(int(len(s) / 2) - 1)] + s[(int(len(s) / 2))]
#     else:
#         return s[(int(len(s) / 2))]

# def get_middle(s):
#    return s[(len(s) - 1) / 2 : len(s) / 2 + 1]
#
# print(get_middle("test"))
# print(get_middle("testing"))
# print(get_middle("middle"))
# print(get_middle("A"))
# print(get_middle("of"))


# 3
# def decode(string):
#     return string.translate(str.maketrans("1234567890", "9876043215"))
#
# print(decode("4103432323")) #6957678787
# print(decode("4103438970")) #6957672135
# print(decode("4104305768")) #6956750342
# print(decode("4102204351")) #6958856709
# print(decode("4107056043")) #6953504567

# 4
# class Solution:
def isPalindrome(x):
    return str(x) == str(x)[::-1]

# solution = Solution.isPalindrome(121)
print(isPalindrome('топт'))

