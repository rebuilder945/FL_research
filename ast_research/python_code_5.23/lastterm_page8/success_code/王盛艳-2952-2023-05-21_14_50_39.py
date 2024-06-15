def print_matrix(n):
    s = ""
    for char in range(1,n+1):
        s += str(char)
    pointer = 1
    for i in range(1,n+1):
        var = s[:pointer] + str(i)*(n-1)
        pointer += 1
        n -= 1
        for char in var:
            print(int(char), end = "")
        print("\n")

number=eval(input())
print_matrix(number)



