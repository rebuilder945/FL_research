def print_matrix(n):
        ls = [0]*number
        for x in range(number):
            for i in range(number):
                if i >= x:
                    ls[i] += 1
            print(ls)

number=eval(input())
print_matrix(number)



