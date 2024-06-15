n=eval(input())
matrix=[x for x in range(1,n+1)]
def demo(matrix,n):
    return (matrix[n-1:]+matrix[:n-1])
print(demo(matrix,n))

