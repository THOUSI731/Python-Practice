num=int(input("Enter Number of Rows: "))
alpha=['A','B','C']
for i in range(num):
     for j in range(ord('A'),ord('E') + 1):
          print(f"{chr(j)} ",end='')
     print()

# =====================================================
               # A B C D E
               # A B C D E
               # A B C D E
               # A B C D E
               # A B C D E
# ============================================================