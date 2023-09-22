from threading import Thread,current_thread

def dispatch_():
     print("Default Child Thread Name",current_thread().name)
     current_thread().setName('doc thread')
     print("New Child Thread Name",current_thread().name)

     
t = Thread(target=dispatch_)
t2 = Thread(target=dispatch_)
t.start()
t2.start()

print("Default Main Thread Name",current_thread().name)
current_thread().setName('Thousi thread Name')
print("New Main Thread Name",current_thread().name)


