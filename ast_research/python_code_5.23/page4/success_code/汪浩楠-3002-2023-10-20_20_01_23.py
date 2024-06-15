ls1=eval(input())
sum=0
for i in ls1:
    sum+=i
    outcome=sum/len(ls1)
if outcome%1!=0:
    print("%.2f"%(outcome))
else:
    a=int(outcome)
    print(a)


