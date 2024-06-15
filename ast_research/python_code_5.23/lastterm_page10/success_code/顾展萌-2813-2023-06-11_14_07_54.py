
s = input().strip()
sub = input().strip()

while sub in s:
    s = s.replace(sub, '')   # 删除子串

print(s)

