def print_matrix(n):
    for x in range(n):
        ls=[]
        for y in range(n):
            if x>=y:
                ls.append(str(y+1))
            else:
                ls.append(str(x+1))
        print(' '.join(ls))

number=eval(input())
print_matrix(number)



