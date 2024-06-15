n,m,l = eval(input())
answer = [n]
for i in range(m-1):
    n = n + l
    answer.append(n)
print(answer)
