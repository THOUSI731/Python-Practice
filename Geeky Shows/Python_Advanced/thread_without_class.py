from threading import Thread

def dis(a,b):
     print("Thread Running",a,"b",b)
     
for i in range(5):
     t=Thread(target=dis,args=(10,20))
     t.start()
     