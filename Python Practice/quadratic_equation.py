import math  
a = int(input("ENTER A VALUE OF A : "))
b = int(input("ENTER A VALUE OF B : "))
c = int(input("ENTER A VALUE OF C : "))
d = b * b - 4 * a * c
if d < 0:
     print("ROOTS ARE IMAGINARY")
else:
     root1 = (-b + math.sqrt(d)) / (2.0 * a)
     root2 = (-b + math.sqrt(d)) / (2.0 * a)
     print("Root 1 = ",root1)
     print("Root 2 = ",root2)
     
