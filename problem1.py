#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution


""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
os.system('cls')
import math

print("Enter in the coefficients for a quadratic equation in the format:")
print("  Ax^2 + Bx + C = 0")
a = input("coeff A: ")
b = input("coeff B: ")
c = input("coeff C: ")


try:
  
  a=float(a)
  b=float(b)
  c=float(c)

  disciminant = b**2 - 4 * a * c
  if disciminant!=0 and a!=0:
    x1 = (-b+math.sqrt(disciminant))/(2*a)
    x2 = (-b-math.sqrt(disciminant))/(2*a)
    print("root 1: ",x1)
    print("root 2: ",x2)
  elif a!=0:
    print("root: ", -b/(2*a))
  else:
    print("root: ", -c/b)
except:
  print("imaganary solution or invalid cahractures")
