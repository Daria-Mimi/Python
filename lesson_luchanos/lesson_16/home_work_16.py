# Написать генераторную функцию которая на вход принимает число n и которая вернёт объект-генератор,
# который по запросу вернёт целые числа от 0 до n.

def give_me_num(num):
    cnt = 0
    while cnt <= num:
        cnt += 1
        yield f"число {cnt}"

some_num = give_me_num(10)
print(next(some_num))
print(next(some_num))
print(next(some_num))
print(next(some_num))
