def print_matrix(n):
    
        string = ""
        for char in range(1, n+1):
            string += str(char)
        pointer = 1
        for i in range(1, n+1):
            var = string[:pointer] + str(i)*(n-1)
            pointer += 1
            n -= 1
            for char in var:
                print(int(char), end="\t")
            print("\n")


number=eval(input())
print_matrix(number)



