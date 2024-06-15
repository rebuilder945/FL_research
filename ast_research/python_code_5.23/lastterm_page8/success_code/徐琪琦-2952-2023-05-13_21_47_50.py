def print_matrix(n):
    s = ""
    for i in range(1,n):
        for a in range(1,i+1):
             s = s +a + " "
        b = str(i +1)
        s += (b+" ")*(n-i)


number=eval(input())
print_matrix(number)



