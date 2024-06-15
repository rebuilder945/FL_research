def print_matrix(n):
    for x in range(1,n+1):
        num = list(range(1,x+1))
        num = [str(y) for y in num]
        s = ' '.join(num)
        s = s + ' ' + (s[-1]+' ')*(n-x)
        print(s.rstrip())

number=eval(input())
print_matrix(number)



