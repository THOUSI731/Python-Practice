class Human:
     def __init__(self,num_heart):
          self.num_eyes = 2
          self.num_nose = 1
          self.num_heart = num_heart
          
     def eat(self):
          print("I can eat")
          
     def work(self):
          print("I can work")
          
class Male(Human):
     def __init__(self,name, num_heart):
          super().__init__(num_heart)
          self.name = name
          
     def smile(self):
          print("I can Smile")
     
     def work(self):
          super().work()
          print("I can Design")
          
     def display(self):
          print(f"Hi,I am {self.name} and i have {self.num_heart} heart and i have {self.num_eyes} eyes")

male=Male("thousi",1)
print(male.num_eyes)
print(male.name)
     
     