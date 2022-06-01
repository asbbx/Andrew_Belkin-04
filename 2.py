# 2. Написать два алгоритма нахождения i-го по счёту простого числа. 
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: 
# Проанализировать скорость и сложность алгоритмов. 

# import cProfile


def eratosthenes(n):
    count = 1
    start = 3
    end = 4 * n

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]
    if n == 1:
        return 2
    while count < n:
        for i in range(len(sieve)):
            if sieve[i] != 0:
                count += 1
                if count == n:
                    return sieve[i]
                j = i + sieve[i]
                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]
        prime.extend([i for i in sieve if i != 0])
        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]
        for i in range(len(sieve)):
            for num in prime:
                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break
 
print(eratosthenes(500))

# cProfile.run('eratosthenes(500)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 2.py:14(<listcomp>)
#         2    0.000    0.000    0.000    0.000 2.py:36(<listcomp>)
#         2    0.000    0.000    0.000    0.000 2.py:39(<listcomp>)
#         1    0.004    0.004    0.005    0.005 2.py:9(eratosthenes)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#      2029    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


def foo(n):
    count = 1
    num = 1
    prime = [2]

    while count != n:
        num += 2
        for i in prime:
            if num % i == 0:
                break
        else:
            count += 1
            prime.append(num)
    return num

print(foo(500))



# cProfile.run('foo(500)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.005    0.005    0.005    0.005 2.py:54(foo)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#       499    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# По статистики, выглядят они, примерно, одинаковыми