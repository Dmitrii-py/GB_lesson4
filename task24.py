"""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты
высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N
кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на
i-ом кусте выросло ni ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система
состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите
программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки."""

from random import randint
list_bush = list(randint(1, 99) for i in range(int(input('Введите кол-во кустов: '))))
print(list_bush)
n = int(input('Введите № куста: '))
count = 0
if n == 1:
    count = list_bush[0] + list_bush[1] + list_bush[-1]
elif n == len(list_bush):
    count = list_bush[-2] + list_bush[-1] + list_bush[0]
else:
    count = list_bush[n - 1] + list_bush[n - 2] + list_bush[n]
print('всего ягод с трех соседних кустов собрали: ', count)
