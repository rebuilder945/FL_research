def list_move_left(A,a):
    for i in range(a):
        A.insert(len(A),A[0])
        A.remove(A[0])
    return A

n = eval(input())
x = [i for i in range(1,n+1)]
print(list_move_left(x,1))
