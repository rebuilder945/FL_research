list = list(eval(input()))
n,m = eval(input())
Q = len(list)
if m<=Q-1:
    list = list[:n]+list[m:]
    print(list)
else:
    print("error")
