a=input()
lst=list(a.split(','))
n, m = input().split(',')
lst[n], lst[m] = lst[m], lst[n]
print(list)
