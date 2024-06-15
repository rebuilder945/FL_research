ls=eval(input())
avg=sum(ls)/len(ls)
if sum(ls)%len(ls)==0:
    print(int(avg))
else:
    print("%.2f"%avg)
