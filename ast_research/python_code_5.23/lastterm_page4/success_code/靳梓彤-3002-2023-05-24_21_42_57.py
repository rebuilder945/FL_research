lst=eval(input())
equ=sum(lst)/len(lst)
if type(equ)==float:
    print("%.2f"%equ)
else:
    print(equ)
