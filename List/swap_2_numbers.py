num1 = int(input("Enter first number to swap: ")) 
num2 = int(input("Enter second number to swap: ")) 

temp=num1
num1=num2
num2=temp

# Easy Method
# num1,num2 = num2,num1

print("Value of First Number After Swapping: ",num1)
print("Value of Second Number After Swapping: ",num2)