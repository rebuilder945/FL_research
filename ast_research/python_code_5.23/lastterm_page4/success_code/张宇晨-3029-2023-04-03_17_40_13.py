Name=input().split(",")
Score=eval(input())
lst=[]
n=len(Name)
for x in range(n):
    ls=[]
    ls.append(Name[x])
    ls.append(Score[x])
    lst.append(ls)
print(lst)
