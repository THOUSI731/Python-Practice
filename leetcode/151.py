def reverseWords(s: str) -> str:
     test=s.strip()
     hi=[]
     for i in test:
          hi.append(i)
     result=''.join(hi).split()
     print(result)
     

     
          
   
print(reverseWords("  helllo world  "))