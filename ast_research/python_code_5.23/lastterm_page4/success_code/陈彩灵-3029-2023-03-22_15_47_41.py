sname=input().split(",")
sgrade=eval(input())
n=len(sname)
ls = []
for x in range(n):
    ls.append([sname[x],sgrade[x]])
print(ls)
