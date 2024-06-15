b=0
ls=[]
while True:
    a=input()
    if a=="#":
        break
    else:
        b+=1
        ls.append(int(a))
print("{} {}".format(b,sum(ls)))
