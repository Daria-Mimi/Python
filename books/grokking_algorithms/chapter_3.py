# def look_for_key(main_box):
#     pile = main_box.make_a_pile_to_look_through()
#     while pile is not empty:
#         bох = pile.grab_a_box()
#         for item in bох:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print("found the key!")

# def look_for_key(bох):
#     for item in bох:
#         if item.is_a_box():
#             look_for_key(item) # рекурсия
#         elif item.is_a_key():
#             print("found the key!")

def binary_search(arr, target):
    if not arr:
        return -1
    if len(arr) == 1 and arr[0] == target:
        return arr[0]
    if len(arr) == 1 and arr[0] != target:
        return -1
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    if arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid+1:], target)



def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(5))
