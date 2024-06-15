a = eval(input())
c = sum(a)/len(a)
for i in c:
    if type(eval(i))==int:
        print(i)
else:
    print("%.2f"%i)
