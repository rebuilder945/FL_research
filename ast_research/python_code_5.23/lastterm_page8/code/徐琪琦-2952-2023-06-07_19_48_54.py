def print_matrix(n):
    print("1 "*n)
        ls = []
        ls1 = []
        for i in range(1,n+1):
            ls1.append(str(i))
        ls1 = " ".join(ls1)
        ls.append(ls1)
        for i in range(n,1,-1):
            ls1 = ls1.replace(str(i),str(i-1))
            ls.append(ls1)
        for i in list(reversed(ls)):
            print(i+"\n")

number=eval(input())
print_matrix(number)



