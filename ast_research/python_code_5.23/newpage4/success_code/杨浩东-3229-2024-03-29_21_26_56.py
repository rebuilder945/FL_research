m=eval(input())
n=list(m)
x=[]
for i in n:
    if n.count(i)<2:
        x.append(i)
print(x)

