#l1 = eval(input())
#l1.sort()
#l1.reverse()
#s = "".join(str(e) for e in l1)
#print(s)
a = eval(input())
a.sort()
a.reverse()
s = 0
def panduan(i):
    for i in a:
        if i == 0:
            return s
        else:
            c = "".join(str(e) for e in a)
            return c
d = panduan(a)
print(d)
        
       
      


   


