def print_matrix(n):
            if n == 1:
                print("1")
            else:
                word="1"
                for i in range(0,n-1):
                    word = word + " 1"
                print(word)
                for i in range (2,n+1):
                    word = "1"
                    lis = [x for x in range(2,i+1)]
                    for j in lis:
                        word = word + " " + str(j)
                    while len(word) != 2*n-1:
                        word = word + " " + str(i)
                    print(word)

number=eval(input())
print_matrix(number)



