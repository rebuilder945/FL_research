lst=eval(input())
i,j=0,0
while i<len(lst):
    if lst[i]==0:
        j=i+1
        while j<len(lst):
            if lst[j]!=0:
                a=lst[i]
                lst[i]=lst[j]
                lst[j]=a
                break
            j+=1
        if j>=len(lst):
            break
    i+=1
print(lst)
