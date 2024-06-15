def list_move_right(A,a):
    for i in range(a):
        A.insert(0,A.pop())
    return A

n = eval(input())
x = [i for i in range(1,n+1)]
print(list_move_right(x,4))
