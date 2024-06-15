num=input()
u=""
for i in num:
    if i.isdigit():
        u=u+i
    else:
        u=u+" "
lst=list(u.split(" "))
lst.sort(reverse=False)
if len(lst)==0:
    print("No digits")
else:
    print(lst[-1])
