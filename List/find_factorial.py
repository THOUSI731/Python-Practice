num=int(input("Enter Your Number To Find Factorial: "))
factorial=1
if num<0:
     print("No Factorial For Negative Numbers")
elif num==0:
     print("Factorial of 0 is 1")
else:
     for i in range(1,num+1):
          factorial *=i
     print("The factorial of",num,"is",factorial)
     