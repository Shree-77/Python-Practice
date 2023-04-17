"""
1.	Write a python program to that accepts length of three sides of a triangle as inputs. The program should indicate whether or not the triangle is a right-angled triangle.
[Hint: Using Pythagorean theorem]
"""
import math 

a=float(input("Enter the length of 1st side: "))
b=float(input("Enter the length of 2nd side : "))

c=math.sqrt(a**2+b**2)

print(c)
