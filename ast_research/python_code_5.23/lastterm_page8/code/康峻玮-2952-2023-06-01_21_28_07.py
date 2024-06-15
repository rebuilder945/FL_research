def print_matrix(n):
    i=1
    num=[]
    while i<=n:
        num.append(list(range(1,i)+[i]*(n+1-i))
        i=i+1
    for x in num:
        for y in x:
            print(y,end=" ")


number=eval(input())
print_matrix(number)



