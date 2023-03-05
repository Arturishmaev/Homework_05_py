task26 = """ Задача 26:  Напишите программу, которая на вход принимает 
два числа A и B, и возводит число А в целую степень B 
с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 """
   
num = int(input("Введите число: "))
exponenta = int(input("Введите степень: "))
def exponentional(num, exponenta):
    if exponenta == 1:
        return num
    return num * exponentional(num, exponenta - 1)

print(f"Результат возведения в степень = {exponentional(num, exponenta)}")
   
 
    
task28 = """ Задача 28: Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел. Из всех 
арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.

*Пример:*

2 2
    4 """
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
def summa(a, b):
    if a == 0:
        return b
    return summa(a - 1, b + 1)
print(f" Сумма чисел = {summa(a,b)}")