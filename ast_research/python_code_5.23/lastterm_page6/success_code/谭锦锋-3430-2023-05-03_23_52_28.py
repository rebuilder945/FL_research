m = {12:"winter",1:"winter",2:"winter",3:"spring",4:"spring",5:"spring",6:"summer",7:"summer",8:"summer",9:"autumn",10:"autumn",11:"autumn"}
a = eval(input())
b = m.get(a)
if b>12:
    print("error")
else:
    print(b)
