def print_matrix(n):
    i=1
    nums=[]
    while i<=n:
        nums.append(list(range(1,i))+[i]*(n+1-i))
        i=i+1
    for x in nums:
        for y in x:
            print(y,end=" ")
        print("")

number=eval(input())
print_matrix(number)



