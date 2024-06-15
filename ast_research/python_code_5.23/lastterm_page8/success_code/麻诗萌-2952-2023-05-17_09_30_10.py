def print_matrix(n):
    for i in range(1,n+1):
        lst=[]
        for x in range(1,i+1):
             lst.append(str(x))
        lst=lst+[str(i)]*(n-i)
        print(" ".join(lst))

number=eval(input())
print_matrix(number)



