lst = input().strip('[').strip(']').split(',')
n, m = map(int, input().split(','))
if n >= m or n < 0 or m > len(lst)-1 or n>len(lst)-1 or m<0:
    print("error")
else:
    del lst[n:m-1]
    print(', '.join(lst))


