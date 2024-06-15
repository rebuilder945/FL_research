m = 1
n = 0
lst = []
while(m):
    a = input()
    if  a!="#":
        n+=1
        lst.append(int(a))
    else:
        m = 0
print(n,sum(lst))

