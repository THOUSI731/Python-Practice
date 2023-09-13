class Parent1 :
     def display(self):
          print("Display From Parent 1 Class")

class Child1(Parent1):
     def display(self):
          print("Display From Child 1 Class")

class Child2(Parent1):
     def display(self):
          print("Display From Child 2 Class")

class Child3(Child1,Child2):
     def display(self):
          print("Display From Child 3 Class")
          
print(Child3.mro())