ls=[0,0,0,0,0]
a=input()
n="~!@#$%^&*()_=-/,.?<>;:[]{"
m="}|\\"
for x in a:
    if x.isnumeric():
        ls[0]=1
    if x.islower():
        ls[1]=1
    if x.isupper():
        ls[2]=1
    if x in m or x in n:
        ls[4]=1
if len(a)>8:
    ls[3]=1
print(ls.count(1))
