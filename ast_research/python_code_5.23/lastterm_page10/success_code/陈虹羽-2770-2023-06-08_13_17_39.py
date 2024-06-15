a=input()
b=input()
if len(a)!=len(b):
   print(False) 
else:
    for i in a:
        if a.count(i)!=b.count(i):
            print(False)
    else:
        print(True)
        
