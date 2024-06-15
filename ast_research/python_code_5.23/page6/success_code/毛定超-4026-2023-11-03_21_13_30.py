list=[2/1,3/2,5/3,8/5,13/8,21/13,34/21,55/34,89/55,144/89,233/144]
t=eval(input())
s=0
x=0
for i in range(t):
    x=x+list[s]
    s=s+1
print("%.4f"%x)


  


