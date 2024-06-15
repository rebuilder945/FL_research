a=eval(input())
def cha(a,v):
    begin,end=0,len(a)-1
    while begin<=end:
        mid=(begin+end)//2
        if a[mid][1]==v:
            s=""
            for x in a[mid]:
                s+=str(x)
            print()
            break
        elif v> a[mid][1]:
            begin=mid+1
        else:
            end=mid-1
    else:
        print("未找到该学生")
