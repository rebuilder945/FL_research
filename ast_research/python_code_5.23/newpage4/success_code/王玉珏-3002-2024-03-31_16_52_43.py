lst=eval(input())
pjz=sum(lst)/len(lst)
if sum(lst)%len(lst)==0:
    print("%.0f"%pjz)
else:
    print("%.2f"%pjz)

