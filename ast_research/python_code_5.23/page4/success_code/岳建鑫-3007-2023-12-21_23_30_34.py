list = input().strip('[]').split(',')
n, m = map(int, input().split(','))
if n > m or n < 1 or m > len(list):
    print("error")
else:
    del list[n-1:m-1]
    print('[{}]'.format(','.join(list)))

