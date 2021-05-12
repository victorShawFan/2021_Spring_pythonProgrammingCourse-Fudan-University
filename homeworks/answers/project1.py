#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-

def celsius_from_fahrenheit(fahrenheit):
    '''华氏度转换到摄氏度'''

    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius



print()
temp_fah = float(input("请您输入华氏度："))
temp_cel = celsius_from_fahrenheit(temp_fah)
print()
print("-"*40)
print()
print(temp_fah,"华氏度转变成摄氏度为",temp_cel) 
print()
print("-"*40)


