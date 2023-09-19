class Student:
     def __init__(self,name,roll_num,age) -> None:
          self.name=name
          self._roll = roll_num #Protected
          self.__age = age  #Private
          
     def get_age(self): # Getter
          return self.__age 
          
     def set_age(self,age):  # Setters
          self.__age=age
          
     def display(self):
          print(f"Hi My Name Is {self.name} age is {self.__age}")
          
s1=Student("Rahul",1,2)
print(s1.get_age())
s1.set_age(10)
s1.display()