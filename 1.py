# 1. Проанализировать скорость и сложность одного любого алгоритма, 
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать 
# несколько реализаций алгоритма и сравнить их.

# Выбрал 1 задачу из 3-его урока

# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import cProfile


def foo():
    result = {}
    for i in range(2, 10):
        result[i] = []
        for j in range(2, 100):
            if j % i == 0:
                result[i].append(j)
        print(f'{len(result[i])} чисел кратны {i} - {result[i]}')

cProfile.run('foo()')

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 1.py:13(foo)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 {built-in method builtins.exec}
#         8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         8    0.001    0.000    0.001    0.000 {built-in method builtins.print}
#       178    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Все предельно быстро выполняется, сложность алгоритма - O(n2) "квадратичная сложность"


min_ = 2
max_ = 9

def div_count(max_number):
    result = {}

    for i in range(min_, max_ + 1):
        result[i] = max_number // i

    return print(result)

cProfile.run('div_count(50)')

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 1.py:40(div_count)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Как видим, при другой реализации, стало еще лучше.