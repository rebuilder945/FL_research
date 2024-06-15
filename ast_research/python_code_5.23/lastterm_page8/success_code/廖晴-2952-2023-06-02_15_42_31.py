def print_matrix(n):
    nums=[]
    i=1
    while i<=n:
        nums.append(list(range(1,i)+[i]*(n-i+1)))
        i+=1
    for x in nums:
        for y in x:
            print(y,end=" ")
        print(end="")

number=eval(input())
print_matrix(number)



