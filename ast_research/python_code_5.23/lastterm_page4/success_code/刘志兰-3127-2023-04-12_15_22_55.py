n = int(input())
s = [i+1 for i in range(n)]   
for i in range(n-1):
    s[i] = s[i+1]
s[n-1] = 1
print(s)
