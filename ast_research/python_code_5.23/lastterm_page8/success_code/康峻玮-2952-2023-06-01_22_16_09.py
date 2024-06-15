def print_matrix(n):
    i=1
    num=[]
    while i<=n:
        num.append(list(range(1,i))+[i]*(n+1-i))
        i+=1
    for y in num:
        print(*y,end="\n",sep=" ")


number=eval(input())
print_matrix(number)



