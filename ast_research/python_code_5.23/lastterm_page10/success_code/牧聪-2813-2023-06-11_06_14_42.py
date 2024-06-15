a=input()
b=input()
if b not in a:
    print(a)
else:
    anew=a.replace(b,"")
    print(anew)
