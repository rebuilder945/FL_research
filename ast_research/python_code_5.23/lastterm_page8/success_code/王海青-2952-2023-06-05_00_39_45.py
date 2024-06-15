def print_matrix(n):
    i=0
    nums=[]
    while i < n:
        line=[3]*(n-1-i)+[1]+[2]*i
        nums.append(line)
        i=i+1
    for x in nums:
        for y in x:
            print(y,end=" ")
        print("")

number=eval(input())
print_matrix(number)



