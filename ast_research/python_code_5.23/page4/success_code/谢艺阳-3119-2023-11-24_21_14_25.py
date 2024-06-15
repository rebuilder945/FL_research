n=eval(input())
n.reverse()
l=[]
for num in n:
    if num not in l:
        l.append(num)
l.reverse()
print(l)
