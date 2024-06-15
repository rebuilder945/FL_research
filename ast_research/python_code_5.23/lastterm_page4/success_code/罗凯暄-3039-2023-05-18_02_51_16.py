ist = eval(input()) 
n=max(ist)
m=min(ist)
newlist2 = []
for i in ist:              #做法1
    if i != n and i != m:
        newlist2.append(i)
print(newlist2)



