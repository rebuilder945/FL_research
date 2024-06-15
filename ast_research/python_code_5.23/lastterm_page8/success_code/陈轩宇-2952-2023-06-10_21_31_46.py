def print_matrix(n):
        matrix=[[0 for c in range(n)]for r in range(n)]
        for r in range(n):
            for c in range(n):
                if r==0 or c==0:
                    matrix[r][c]=1
                elif c==1 and r>=1 or c>=1 and r==1:
                    matrix[r][c]=2
                elif c==2 and r>=2 or c>=2 and r==2:
                    matrix[r][c]=3
                elif c==3 and r>=3 or c>=3 and r==3:
                    matrix[r][c]=4
                else:
                    matrix[r][c]=5
        for r in range(n):
            for c in range(n):
                print(matrix[r][c],end="")
            print()
        

number=eval(input())
print_matrix(number)



