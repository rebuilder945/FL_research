def print_matrix(n):
        ls=[]
        i=0
        for x in range(n):
            ls.append('1')
        while True:
            if i==n:
                break
            else:
                print(' '.join(ls))
                i+=1
                del ls[i:n]
                for x in range(n-i):
                    ls.append(str(i+1))

number=eval(input())
print_matrix(number)



