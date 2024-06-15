n=eval(input())
ls=list(range(1,13))
if n in range(1,13):
    for x in range(13):
        if x in [3,4,5]:
            ls[x]="spring"
        elif x in [6,7,8]:
            ls[x]="summer"
        elif x in [9,10,11]:
            ls[x]="autumn"
        else:
            ls[x]="winter"
    print(ls[n])
else:
    print("error")
