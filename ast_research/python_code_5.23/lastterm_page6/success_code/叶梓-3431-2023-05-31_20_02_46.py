n=eval(input())
List=list(range(0,37))
if n in range(0,37):
    for x in range(0,37):
        if x==0:
            List[x]="green"
        elif x in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 29, 30, 32, 34, 36]:
            List[x]="red"
        else:
            List[x]="black"
    print(List[n])
else:
    print("error")

