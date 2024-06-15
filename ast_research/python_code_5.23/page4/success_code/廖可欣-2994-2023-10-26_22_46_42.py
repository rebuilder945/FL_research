ele = eval(input())
n,m = eval(input())
element = list(ele)
if n > len(element):
    print("error")
else:
    xuyao = element[n]
    biao = [xuyao]*m
    end = element + biao
    print(end)
