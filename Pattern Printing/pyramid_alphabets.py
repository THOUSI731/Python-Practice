num=int(input("Enter Number Of Rows: "))
alpha=['A','B','C','D','E']
for i,j in enumerate(alpha):
     for k in range(i+1):
          print(f"{j} ",end='')
     print()
     
# =======================================
               # A
               # B B
               # C C C
               # D D D D
               # E E E E E
# =======================================