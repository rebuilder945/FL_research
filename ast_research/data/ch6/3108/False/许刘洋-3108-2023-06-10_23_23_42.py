lst = eval(input())
b=''
for i in lst:
    for j in i:
        b+=j
for i in b:
    s=b.count(i)
    print(i,s)
