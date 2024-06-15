s = input().strip()
i = j = -1   # 初始化最长数字子串的起始和结束位置
for k in range(len(s)):
    if s[k].isdigit():
        if i == -1:
            i = j = k
        else:
            j = k
    else:
        i = -1
if i == -1:
    print("No digits")
else:
    print(s[i:j+1])
