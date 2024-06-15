def ci(a:str):
    return int(a)**3
s=int(input())
flag = False
if 100<s<1000:
    for i in range(100,s+1):
        if sum(map(ci,str(i)))==i:
            print(i)
            falg=True
if not flag:
    print("none")
