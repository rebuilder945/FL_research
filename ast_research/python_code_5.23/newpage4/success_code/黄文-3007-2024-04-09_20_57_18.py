input_list=eval(input())
n,m=map(int,input().split(','))
if n <= m:
    result_list = [x for x in input_list if x >= n or x < m]
    print(result_list)
else:
    print(error)
       
