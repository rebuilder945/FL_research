a_all=eval(input())
a_average=sum(a_all)/len(a_all)
if sum(a_all)%len(a_all)==0:
    print("%.d"%a_average)
else:
    print("%.2f"%a_average)
