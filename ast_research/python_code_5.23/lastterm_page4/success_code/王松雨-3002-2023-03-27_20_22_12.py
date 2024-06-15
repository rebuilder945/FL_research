lst=eval(input())
for x in lst[:]:
    a=sum(x)/len(lst)
    if a is int:
        print(a)
    if a is float:
        print("%.2f"%a)
