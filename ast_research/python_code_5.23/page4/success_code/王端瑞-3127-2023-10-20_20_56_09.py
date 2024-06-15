n = eval(input())

matrix = [i+1 for i in range(n)]

matrix2 = []

for m in matrix:

    if m<max(matrix):

        m+=1

        matrix2.append(m)

    else:

        m=min(matrix)

        matrix2.append(m)

print(matrix2)
