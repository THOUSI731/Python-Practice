num = int(input("Enter Number of Rows: "))
for i in range(num):
     for space in range(i,num):
          print(" ",end='')
     
     for star in range(i+1):
          print("*",end='')
     print()