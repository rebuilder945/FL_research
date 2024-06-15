def print_matrix(n):
            for i in range(n):
                    print("",end="\n")
                    for x in range(n):
                            if x>=i:
                                    print(i+1,end=" ")
                            else:
                                    print(x+1,end="")

number=eval(input())
print_matrix(number)



