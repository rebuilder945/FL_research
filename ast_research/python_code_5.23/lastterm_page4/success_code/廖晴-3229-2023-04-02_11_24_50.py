s=eval(input())
t=[]
for x in s:
     if s.count(x)<=1:
          t.append(x)
t.sort()
if len(t)>=1:
        print(",".join(map(str,t)))
else:
     print("False")
