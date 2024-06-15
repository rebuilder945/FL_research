s = input()
max_digit = ""
cur = ""
for c in s:
    if c.isdigit():
        cur += c
    else:
        if len(cur) > 0:
            if len(cur) >= len(max_digit):
                max_digit = cur
            cur = ""
if len(cur) > 0:
    if len(cur) >= len(max_digit):
        max_digit = cur

if not max_digit:
    print("No digits")
else:
    print(max_digit)
