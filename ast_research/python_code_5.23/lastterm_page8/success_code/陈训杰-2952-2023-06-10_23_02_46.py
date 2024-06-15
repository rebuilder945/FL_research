def print_matrix(n):
    ju=[[min([x+1,y+1]) for x in range(n)]for y in range(n)]
    for i in ju:
        i=map(str,i)
        print(" ".join(i))

number=eval(input())
print_matrix(number)



