lit=input().split()
n,m=list(map(eval,input().split()))
lit[m],lit[n]=lit[n],lit[m]
print(lit)
