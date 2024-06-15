a=eval(input())
for i in a:
     c=2
     while i>c:
          if i%c==0:
               a.remove(i)
          c+=1
     print(a)
     

