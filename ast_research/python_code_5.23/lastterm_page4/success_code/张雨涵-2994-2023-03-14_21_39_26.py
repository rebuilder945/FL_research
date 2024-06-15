ls = list(eval(input()))
m,n = eval(input())
if m<len(ls):
    b = [int(ls[m])]*n
    print(ls+b)
else:
    print("error")
