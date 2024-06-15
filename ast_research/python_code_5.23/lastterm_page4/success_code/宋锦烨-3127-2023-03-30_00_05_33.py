a=int(input())
b=[x*1 for x in range(1,a+1)]
def list_move_left(A,a):
    for i in range(a):
        A.insert(len(A),A[0])
        A.remove(A[0])
    return A
print(list_move_left(b,1))
