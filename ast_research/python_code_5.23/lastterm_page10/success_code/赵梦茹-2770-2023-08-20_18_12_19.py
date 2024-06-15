a=input()
b=input()
c=0
for i in a:
    if i in b:
        continue
    else:
       c=1
if c==0 and  len(a)==len(b):
         print("True")
else:
     print("False")
