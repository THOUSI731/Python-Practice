from Abstract_class import Store

class Story(Store):
     def __init__(self,n):
          super().__init__(n)          
     def read(self):
          print("I am Reading My Book",self.num_books)
          

class Novel:
     def __init__(self):
          self.num_books = 10
          
     def read(self):
          print("I am Reading My Novel")
     

class Horror:
     def __init__(self):
          self.num_books = 10
          
     def read(self):
          print("I am Reading Horror Story")
          

v=Story(10)
v.read()
