"""
https://www.codewars.com/kata/555086d53eac039a2a000083
https://www.codewars.com/kata/5865918c6b569962950002a1
https://www.codewars.com/kata/50654ddff44f800200000007
https://www.codewars.com/kata/61123a6f2446320021db987d
https://www.codewars.com/kata/5977618080ef220766000022

"""
#1
# def lovefunc( flower1, flower2 ):
#     return flower1 % 2 != flower2 % 2
#
# def lovefunc( flower1, flower2 ):
#     return (flower1+flower2)%2

#2
# def str_count(strng, letter):
#     return (strng.count(letter))
#
# def str_count(strng, letter):
#     if letter in strng:
#         res = 0
#         for i in strng:
#             if letter in strng[strng.index(i):(int(len(letter)) + int(strng.index(i)))]:
#                 res += 1
#         return res
#     else:
#         return 0
#
# print(str_count("hello", "p"))

#3
# def solution(a, b):
#     if len(a) < len(b):
#         return a + b + a
#     else:
#         len(b) < len(a)
#         return b + a + b
#
# print(solution("el", "a"))
#
# def solution(a, b):
#     return a+b+a if len(a)<len(b) else b+a+b

#4
# def prev_mult_of_three(n):
#     while n % 3 != 0:
#         n //= 10
#         if n == 0:
#             return
#     return n
#
# print(prev_mult_of_three(25))
# print(prev_mult_of_three(1244))
# print(prev_mult_of_three(952406))
#
# def prev_mult_of_three(n):
#     while n % 3:
#         n //= 10
#     return n or None

#5
def usdcny(usd):
    cny = 6.75
    res = usd * cny
    return f"{res:.2f} Chinese Yuan"

print(usdcny(2994))

