def print_matrix(n):
    s = ""
    for i in range(1,n):
        for a in range(1,i+1):
            s = s +str(a) + " "
        b = str(i +1)
        s += (b+" ")*(n-i)
        print(s)


number=eval(input())
print_matrix(number)



