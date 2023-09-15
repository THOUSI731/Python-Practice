# 1 :- Number Should Greater Than 1
# 2 :- Number has only two factors 1 and itself

num=int(input("Enter the number to check Prime or Not: "))
count=0        # check how many factors are there
if num > 1:
     for i in range(1,num+1):
          if num%i==0:
               count += 1
     
     if count == 2:
          print("Prime Number")
     else:
          print("Not Prime Number")