s = input().strip()  # 获取输入字符串，并清除前后的空格

if not any(c.isdigit() for c in s):  # 判断是否含有数字字符
    print("No digits")
else:
    res = ""
    cur = ""

    for c in s:
        if c.isdigit():
            cur += c
        else:
            if len(cur) > len(res):
                res = cur
            cur = ""

    
    print(res)s
