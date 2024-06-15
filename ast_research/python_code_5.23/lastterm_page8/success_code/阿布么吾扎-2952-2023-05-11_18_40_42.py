def print_matrix(n):
    for x in range(n):#数字去行数和列数里面最小的那一个
        for y in range(n):
            print(min(x,y)+1,end=' ')#取的比本身的小1
        print()

number=eval(input())
print_matrix(number)



