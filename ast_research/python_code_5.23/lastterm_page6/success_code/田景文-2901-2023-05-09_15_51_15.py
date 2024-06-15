i = 0
s = 0
m = 1
while(m):
    x = input()
    if(x!="#"):
        s+=int(x)
        i+=1
    else:
        m = 0
print(i,s)
