def print_matrix(n):
            for i in range(1,n+1):
                    c=[]
                    for x in range(1,n+1):
                            if i==x:
                                    for e in range(n-x+1):
                                            c.append(str(x))
                                  
                                    print(' '.join(c))
                                    break
                            else:
                                    c.append(str(x))

number=eval(input())
print_matrix(number)



