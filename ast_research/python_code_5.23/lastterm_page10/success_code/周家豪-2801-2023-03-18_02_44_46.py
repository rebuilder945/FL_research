code=input()
k=0
if len(code)<=28:
    for x in code:
        if x.isdigit():
            k+=1
            break
    for x in code:
        if x.islower():
            k+=1
            break
    for x in code:
        if x.isupper():
            k+=1
            break
    if len(code)>=8:
        k+=1
    for x in code:
        if x in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\":
            k+=1
            break
    print(k)

