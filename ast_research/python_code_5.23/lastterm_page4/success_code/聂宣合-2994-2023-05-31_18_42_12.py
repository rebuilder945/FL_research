lst=list(eval(input()))
n,m=input().split(",")
x=[]

if n>len(lst):
    print("error")
else:
    x.append(lst[int(n)])
    print(lst+(x)*int(m))
