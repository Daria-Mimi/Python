# quicksort быстрая сортировка

def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 7, 9, 2, 3]))

#  функция для суммы всех элементов в списке
# def sum(arr):
#   total = 0
#   for x in arr:
#     total += x
#   return total
#
# print(sum([1, 2, 3, 4]))

# def sum(list):
#   if list == []:
#     return 0
#   return list[0] + sum(list[1:])
#
# print(sum([1, 2, 3, 4, 5]))

# рекурсивная функция для подсчета элементов в списке
# def count(list):
#   if list == []:
#     return 0
#   return 1 + count(list[1:])
#
# print(count([1, 2, 3, 4, 5]))


