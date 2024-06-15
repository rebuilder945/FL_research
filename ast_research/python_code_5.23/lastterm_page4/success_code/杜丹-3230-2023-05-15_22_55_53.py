lst=eval(input())
def maxsort(lst):
    n=len(lst)
    for i in range(n-1):
        for j in range(n-1-i):
            if str(lst[j])+str(lst[j+1])<str(lst[j+1])+str(lst[j]):
                lst[j],lst[j+1]=lst[j+1],lst[j]
    s=''
    for a in lst:
        s=s+str(a)
    return int(s)
print(maxsort(lst))


