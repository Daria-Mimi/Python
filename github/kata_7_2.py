"""
https://www.codewars.com/kata/5effa412233ac3002a9e471d ???
https://www.codewars.com/kata/5a03b3f6a1c9040084001765

"""
#2

# def angle(n):
#     return (n - 2) * 180
#
# print(angle(3))
# print(angle(4))


number = int(input("Enter an integer number "))
if number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')