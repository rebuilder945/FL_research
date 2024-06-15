def print_matrix(n):
        for i in range(n):
            c=[]
            for x in range(n):
                if x<i+1:
                    c.append(x+1)
                else:
                    c.append(i+1)
            c=[str(i) for i in c]
            print(' '.join(c))
            c=[]

number=eval(input())
print_matrix(number)



