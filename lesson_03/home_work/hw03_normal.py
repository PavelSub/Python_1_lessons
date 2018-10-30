from random import randint


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fib(n, m):
    li, i = [1, 1], 0
    while i < m:
        li.append(li[i] + li[i + 1])
        i += 1
    return li[n - 1:m]


print(fib(4, 8))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def q_sort(i_1, start, end):
    if start < end:
        pivot = randint(start, end)
        i_1[end], i_1[pivot] = i_1[pivot], i_1[end]
        split = part(i_1, start, end)
        q_sort(i_1, start, split - 1)
        q_sort(i_1, split + 1, end)


def part(i_1, start, end):
    p_i = start - 1
    for ind in range(start, end):
        if i_1[ind] < i_1[end]:
            p_i += 1
            i_1[p_i], i_1[ind] = i_1[ind], i_1[p_i]
    i_1[p_i + 1], i_1[end] = i_1[end], i_1[p_i + 1]
    return p_i + 1


nums = [1, 12, 5, 8, -5, 17, 15, -2, 9]
q_sort(nums, 0, len(nums) - 1)
print(nums)


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def fil(l, f):
    return [i for i in l if i != f]


nums = [1, 12, 5, 8, -5, 17, 15, -2, 9]
f = 8
print(fil(nums, f))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def par(x1, y1, x2, y2, x3, y3, x4, y4):
    t1, t2, t3, t4 = [x1, y1], [x2, y2], [x3, y3], [x4, y4]
    d1 = [(t3[0] + t1[0]) / 2, (t3[1] + t1[1]) / 2]
    d2 = [(t4[0] + t2[0]) / 2, (t2[1] + t4[1]) / 2]
    if t3[0] - t2[0] == t4[0] - t1[0] and t2[1] - t1[1] == t3[1] - t4[1] and d1[0] == d2[0] and d1[1] == d2[1]:
        res = 'Это параллелограмм!'
    else:
        res = 'Это НЕ параллелограмм!'
    return res


х1, у1, x2, у2, x3, у3, х4, у4 = 2, 2, 3, 4, 6, 4, 5, 2
print(par(х1, у1, x2, у2, x3, у3, х4, у4))
