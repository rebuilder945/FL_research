list=eval(input())
a=0
for i in list:
    a+=i
b=len(list)
c=a/b
if a%b==0:
    print(int(c))
else:
    print("%.2f"%(c))

