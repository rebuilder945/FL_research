list=input().split()
n,m=map(int. input().split())
temp=list[n]
list[n]=list[m]
list[m]=temp
print(list)
