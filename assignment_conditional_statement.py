# -*- coding: utf-8 -*-
"""Assignment_conditional_Statement.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-iBab_kUzimIfkVVJjUjufPA1AxQZUEM
"""

x=int(input("Enter any number to check for prime number or not "))
for i in range(2,x):
  if(x%i==0):
    print("Number entered is not a prime number")
    break
else:
  print("Number entered is a prime number")

x=int(input("Enter a positive integer to check for its divisibility by 3 : "))
sum=0
while(x>0):
  digit=x%10
  sum =sum+digit
  x=x//10
if(sum%3==0):
  print(" Entered number is divisible by 3")
else:
  print("Entered number is not divisible by 3")