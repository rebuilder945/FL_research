str1=input()
n,m=map(int,input().split(' '))
lst1=[str(n) for n in str1.split(' ')]
if n>len(lst1):
    print("error")
elif m>>len(lst1):
    print("error")
else:
    eva=lst1[n]
    lst1[n]=lst1[m]
    lst1[m]=eva
print(lst1)
