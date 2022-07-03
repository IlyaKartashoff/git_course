# Пузырьковая сортировка
from random import randint
import time


def nask(amin, amax):
    if amin <= 20:
        amin = 20
    else:
        pass
    if amax > 1000:
        amax = 1000
    while True:
        try:
            a = int(input(f'Введите количество чисел для сортировки (от {amin} до {amax}): '))
            if amin <= a <= amax:
                break
            elif a < amin:
                print('Число меньше минимальной границы, повторите ввод.')
                continue
            elif a > amax:
                print('Число больше максимальной границы, повторите ввод.')
        except ValueError:
            print('Не верный ввод. Попробуйте снова.')
    return a


x = nask(20, 1000)

list_for_sort = [randint(10000, 99999) for _ in range(x)]


def bub_sort(some_list):
    sl = some_list
    for i in range(len(some_list) - 1):
        for j in range(len(some_list) - 2, i - 1, -1):
            if sl[j + 1] < sl[j]:
                sl[j], sl[j + 1] = sl[j + 1], sl[j]


st = time.process_time()
bub_sort(list_for_sort)
ft = time.process_time()
op_time = ft - st
print(len(list_for_sort))
print(f"{op_time:.3f}")
print(sum(list_for_sort[-1:-11:-1]))
print(sum(list_for_sort[0:10:1]))
