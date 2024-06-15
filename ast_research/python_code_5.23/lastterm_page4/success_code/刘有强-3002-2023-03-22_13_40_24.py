dongxi=eval(input())
average1=sum(dongxi)/len(dongxi)
if average1-int(average1) == 0:
    print(int(average1))
else:
    print("%.2f"%average1)
