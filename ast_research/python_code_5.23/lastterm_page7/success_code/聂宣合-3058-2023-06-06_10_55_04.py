dics={}
while True:
    n=input()
    if n=="q":
        break
    else:
        dics[n]=dics.get(n,0)+1

lst=list(dics.items())

lst.sort(key=lambda x:x[1])

z=lst[-1]

print("{} {}".format(z[0],z[1]))
