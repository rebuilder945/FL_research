n = eval(input())
n.sort(reverse=True)
a = ""
for i in range(0,len(n)):
    a = a + str(n[i])
print(int(a))
