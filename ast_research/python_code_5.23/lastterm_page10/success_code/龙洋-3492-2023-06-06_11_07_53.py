x=input()or'None'
if x=='None':
    print(x)
else:
    for y in x:
        if x.count(y)==1:
            print(y)

