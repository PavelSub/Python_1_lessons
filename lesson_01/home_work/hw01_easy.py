
__author__ = 'Субботин Павел Юрьевич'

# Задача-1: Запросите у пользователя ввод произвольного целого числа
# Необходимо вывести поочередно цифры введенного пользователем числа

aa = input('Введите произвольное целое число: ')
for a in aa:
   print(a)

# Задача-2: Запросите у пользователя ввод двух чисел и связать значения с соответствующими переменными
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a, b = input('Введите целое число'), input('Введите целое число')
a, b = b, a
print(a ,',',b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = input('Введите свой возраст: ')
if age >= 18:
    print('Доступ разрешен!')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')

