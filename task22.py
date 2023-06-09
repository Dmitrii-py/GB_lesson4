"""Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
 m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
from random import randint

n_set = set(randint(1, 99) for x in range(int(input('Введите кол-во чисел первого набора : '))))
print(n_set)
m_set = set(randint(1, 99) for y in range(int(input('Введите кол-во чисел второго набора: '))))
print(m_set)
x_set = sorted(n_set.intersection(m_set))
print(*x_set, sep=", ")
