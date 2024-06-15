def print_matrix(n):
        for i in range(n):
            t = 1
            for m in range(n):
                if t < i+1 and m != n-1:
                    print(t,end=' ')
                    t += 1
                elif  t == i+1 and m != n-1:
                    print(t,end=' ')
                else:
                    print(t)

number=eval(input())
print_matrix(number)



