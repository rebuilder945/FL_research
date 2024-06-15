a=input()
lst=list(a.split(','))
n, m = eval(input())
lst[n], lst[m] = lst[m], lst[n]
print(list)
