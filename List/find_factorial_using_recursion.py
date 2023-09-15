num = int(input("Enter Number To Find Factorial: "))
def factorial(n):
     if n==0 or n==1:
          return 1  # stop the iteration
     else:
          return n*factorial(n-1)
     
     # return 1 if n==0 or n==1 else n*factorial(n-1) # Ternary Operator
     
print(factorial(num))