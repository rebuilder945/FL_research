def print_matrix(n):
    i = 1
    nums = []
    while i<=n:
        nums.append(list(range(1,i))+([i]*(n-i+1)))
        i+=1
    for item in nums:
        print(*item,end='\n',sep=" ")

number=eval(input())
print_matrix(number)



