str1=input()
n,m=map(int,input().split(','))
lst1=list(str1.split(' '))
lst1[n],lst1[m]=lst1[m],lst1[n]
print(lst1)
