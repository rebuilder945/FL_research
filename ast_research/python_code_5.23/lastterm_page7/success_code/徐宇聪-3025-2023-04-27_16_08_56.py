s = input().split(' ')
len_s = 0
for i in s:
    len_s += len(i)
print(f"{len(s)},{len_s/len(s):.2f}")
