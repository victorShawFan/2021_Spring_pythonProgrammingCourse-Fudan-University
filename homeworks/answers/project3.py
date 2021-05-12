#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-

""" Project 3 直角三角形和其形成的锥形
提示用户输入直角三角形的底边和高，计算出直角三角形的周长面积以及旋转
直角三角形形成锥形的表面积和体积，计算结果保留3位小数。
    perimeter = radius + height + math.sqrt(radius ** 2 + height ** 2)
    area = (radius * height) / 2
    volume = math.pi * radius ** 2 * height / 3
    surface = math.pi * radius * (radius + math.sqrt(radius ** 2 + height ** 2))

""" 

import math

def compute_cone_surface(radius, height):
    surface = math.pi * radius * (radius + math.sqrt(radius ** 2 + height ** 2))
    return surface

def compute_cone_volume(radius, height):
    volume = math.pi * radius ** 2 * height / 3
    return volume

def compute_right_triangle_perimeter(radius, height):
    perimeter = radius + height + math.sqrt(radius ** 2 + height ** 2)
    return perimeter

def compute_right_triangle_area(radius, height):
    return (radius * height) / 2

def main():
    radius = input("请输入直角三角形的底边长度 >>> ")
    radius = float(radius)

    height = input("请输入直角三角形的高长度   >>> ")
    height = float(height)

    area = compute_right_triangle_area(radius, height)
    perimeter = compute_right_triangle_perimeter(radius, height)
    surface = compute_cone_surface(radius, height)
    volume = compute_cone_volume(radius, height) 

    
    print()
    print("-"*40)
    print()
    print("       直角三角形的底边长 = %9.3f" % radius)
    print("         直角三角形的高长 = %9.3f" % height)

    print("         直角三角形的面积 = %9.3f" % area)
    print("         直角三角形的周长 = %9.3f" % perimeter)
 
    print("             锥形的表面积 = %9.3f" % surface)
    print("               锥形的体积 = %9.3f" % volume)
    print()
    print("-"*40)


if __name__ == '__main__':
    main()
