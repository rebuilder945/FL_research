list = input().strip('[]').split(',')
n, m = map(int, input().split(','))
if n > m or n < 0 or m > len(list)-1:
    print("error")
else:
    del list[n:m-1]
    print('[{}]'.format(','.join(list)))

