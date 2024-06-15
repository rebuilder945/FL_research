s=eval(input())
t=[]
for x in s:
    for i in range(s.count(x)):
         s.remove(x)
s.sort()
if len(s)>=1:
     print(s)
else:
     print("False")
