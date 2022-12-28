# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math

def simplemultiplier(n):
   while n % 2 == 0:
      n = n / 2
   
   for i in range(3,int(math.sqrt(n))+1,2):
      while (n % i == 0):
         n = n / i
   
   if n > 2:
      print (n)

n = int(input("Введите число для вычисления простых множителей :"))  
simplemultiplier(n)