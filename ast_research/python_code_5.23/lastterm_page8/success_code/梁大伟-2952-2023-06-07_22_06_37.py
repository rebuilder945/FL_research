def print_matrix(n):
    s=''
    l=[str(x+1) for x in range(9)]
    for i in range(n):
        ls=[l[i]]*(n-i)
        s=' '.join(l[0:i]+ls)
        print(s)

number=eval(input())
print_matrix(number)



