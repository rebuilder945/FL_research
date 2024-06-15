def print_matrix(n):
    for i in range(1, n+1):
            for j in range(1, n+1):
                # 输出第 i 行第 j 列的元素
                print(min(i, j), end=' ')
            # 每行结束时换行
            print()
    
        

number=eval(input())
print_matrix(number)



