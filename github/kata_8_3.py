"""
https://www.codewars.com/kata/58649884a1659ed6cb000072
https://www.codewars.com/kata/583710ccaa6717322c000105
https://www.codewars.com/kata/57a4d500e298a7952100035d
https://www.codewars.com/kata/5a360620f28b82a711000047
https://www.codewars.com/kata/551b4501ac0447318f0009cd


"""

# 1
# def update_light(current):
#     if current == "green":
#         return "yellow"
#     if current == "yellow":
#         return "red"
#     if current == "red":
#         return "green"
#
# print(update_light("red"))
# print(update_light("green"))
# print(update_light("yellow"))
#
# def update_light(current):
#     return {"green": "yellow", "yellow": "red", "red": "green"}[current]
#
#
# def update_light(current):
#     light_order = {'red': 'green', 'yellow': 'red', 'green': 'yellow'}
#
#     return light_order[current]

# 2
# def simple_multiplication(number):
#     if number % 2 == 0:
#         return number * 8
#     else:
#         return number * 9
#
# print(simple_multiplication(8))
# print(simple_multiplication(3))
# print(simple_multiplication(1))
# print(simple_multiplication(2))
#
# def simple_multiplication(number) :
#     return number * 9 if number % 2 else number * 8
#
# def simple_multiplication(number) :
#     return number * 8 if number % 2 == 0 else number * 9

# 3
# def hex_to_dec(s):
#     return int(s, 16)
#
# print(hex_to_dec("1"))
# print(hex_to_dec("a"))
# print(hex_to_dec("10"))

# 4
# DECK = ['2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS',
#         '2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD',
#         '2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH',
#         '2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC']
#
# def define_suit(card):
#     if "C" in card:
#         return 'clubs'
#     elif "D" in card:
#         return 'diamonds'
#     elif "H" in card:
#         return 'hearts'
#     elif "S" in card:
#         return 'spades'
#
# print(define_suit("6D"))
# print(define_suit("6H"))
# print(define_suit("6S"))

# def define_suit(card):
#     return {'C':'clubs', 'S':'spades', 'D':'diamonds', 'H':'hearts'}[card[-1]]
#
# print(define_suit("6D"))
# print(define_suit("6H"))
# print(define_suit("6S"))

# 5
# def boolean_to_string(b):
#     if b == bool(True):
#         return "True"
#     else:
#         return "False"

# def boolean_to_string(b):
#     return 'True' if b else 'False'

# print(boolean_to_string(1))
# print(boolean_to_string(0))
# print(boolean_to_string(1))
# print(boolean_to_string(0))

# 6
