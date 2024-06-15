def sxh(n):
    List1 = []
    if n <=100:
        print("none")
    elif n<1000:
        List =[int(i) for i in range(101,n+1)]
    elif n>=1000:
        List =[int(i) for i in range(101,1000)]
    for i in range(len(List)):
        for x in list(str(List[i])):
            if sum((int(x))**3) == List[i]:
                List1.append(List[i])
    if List1 == []:
            print("none")
    else:
        for a in List1:
            print(a)
n  =eval(input())
sxh(n)
