a=input()
b=int(sum(a))/int(len(a))
if type(b)==int:
    print(b)
else:
    print("%.2f"%b)
