a=input()
b=input()
p=0
if len(a)==len(b):
   for i in a:
      for j in b:
         if a.count(i)==b.count(i) and b.count(j)==a.count(j):
            p=1
         else:
            p=0
   if p ==1:
      print('True')
if p==0:
   print('False')

