from abc import ABC,abstractmethod

class Store(ABC):
     def __init__(self,n):
          self.num_books = n
          
     @abstractmethod
     def read(self):
          pass
     
     def display(self):  # Concrete Method
          print("Hi iam Concrete Method")

# v=Store(0)


