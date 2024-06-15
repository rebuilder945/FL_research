ls=eval(input())
avg=sum(ls)/len(ls)
if avg==int(avg):
    print(avg)
else:
    print(".2f"%avg)
