ls = list(eval(input()))
n,m = eval(input())
if n>len(ls)-1:
    print("error")
else:
    for i in range(m):
        ls.append(ls[n+1]) 
    print(ls)       
