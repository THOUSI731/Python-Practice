# Palindrome ===========================================>
"""
def palindrome(s):
     return s == s[::-1]

s  = input("Enter the word:")
if palindrome(s):
     print("Its a Palindrome")
else:
     print("Naah Its Not")
"""

# Local And Global Variables ===============================>
"""
def change(a):
     a = 90
     print(f"Inside of the function {a}") # 90

a = 1
print(f"Before Function Call {a}") # 1
change(a)
print(f"After Function Call {a}") # 1
"""
"""
def change(b):
     global a
     a = 90
     print(f"Inside of the function {a}") # 90

a = 1
print(f"Before Function Call {a}") # 1
change(a) 
print(f"After Function Call {a}") # 90
"""
# Default Argument Value =========================================>
"""
def test(a,b=0):
     if a > b:
          return True
     else:
          return False
     
     
print(test(-10))
"""
"""  
def f(a,data=[]):
     data.append(a)
     return data

print(f(3)) # [3]
print(f(90)) # [3,90]
"""
"""
def f(a,data=None):
     if data is None:
          data = []
     data.append(a)
     return data

print(f(1))  # [1]
print(f(90))  # [90]
print(f(10000)) # [10000]
"""

# Keyword Arguments ================================================>
"""  
def func(a, b=5, c=10):
     print('a is', a, 'and b is', b, 'and c is', c)

func(12, 24)
""" 