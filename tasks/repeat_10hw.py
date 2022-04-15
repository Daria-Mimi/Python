# res = []
# for el in range(100):
#     if el % 3 == 0:
#         res.append(el)
#
# print(res)


# res = []
# user = input('Введите числа, разделенные пробелом: ').split()
# for el in user:
#     res.append(int(el))
#
# print(res)
#
# res1 = [x for x in res if x % 2 == 0]
# print(res1)
#
# user2 = input("Введите символ, который хотите использовать в качестве разделителя: ")
# string = f'{user2}'.join(str(x2) for x2 in sorted(res1))
# print(string)



# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         res = list[mid]
#         if res == item:
#             return mid
#         elif res > item:
#             high = mid - 1
#         elif res < item:
#             low = mid + 1
#         else:
#             return None


# my_list = [1, 3, 5, 7, 9]
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# print(binary_search(my_list, 3))
# print(binary_search(my_list, 8))
# print(binary_search(my_list, 9))
# print(binary_search(my_list, 32))


