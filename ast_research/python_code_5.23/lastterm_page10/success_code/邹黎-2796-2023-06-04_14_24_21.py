a=input()
for x in a:
    if x not in list("0123456789"):
        a=a.replace(x," ")
        
if a.isalpha() or a==" ":
    print("No digits")
else:
    lst=a.split()

    max=0
    for x in lst:
        if len(x)>=max:
            max=len(x)
    for x in reversed(lst):
        if len(x)==max:   
            print(x)
            break

