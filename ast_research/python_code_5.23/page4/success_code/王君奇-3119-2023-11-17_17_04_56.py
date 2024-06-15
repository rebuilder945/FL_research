x=eval(input())
y=[]
for i in x:
    if i not in y:
        y.insert(0,i)
print(y)
