n = eval(input())
ls = [x for x in range(1,n+1)]
# A为原始列表，a为左移位数
def list_move_left(A,a):
    for i in range(a):
        A.insert(len(A),A[0])
        A.remove(A[0])
    return A
print(list_move_left(ls,1))    

