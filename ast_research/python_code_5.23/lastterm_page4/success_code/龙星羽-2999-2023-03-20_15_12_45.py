lie=input().split(' ')
n,m= list(map(int, input().strip().split()))
lie[n],lie[m]=lie[m],lie[n]
print(lie)
