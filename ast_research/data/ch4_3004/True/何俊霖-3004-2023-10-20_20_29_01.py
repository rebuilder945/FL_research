from os import remove


x=list(eval(input()))
y=[0,1]
for i in x:
    if i==2:
        x=x
    else:
        for n in range(2,i):
            if i%n==0:
                y.append(i)
e=[i for i in x if i not in y]
print(e)

