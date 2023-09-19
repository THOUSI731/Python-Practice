class Student:
     def __init__(self,name,roll_num,age) -> None:
          self.name=name
          self._roll = roll_num #Protected
          self.__age = age  #Private
          
     def display(self):
          print(f"Hi My Name Is {self.name}")
          
# s1=Student("Rahul",1,1)
# s1.display()

# print(dir(s1)) # name mangling to access private atrributes or methods


