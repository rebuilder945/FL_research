symbols=r"~!@#$%^&*()_=-/,.?<>;:[]{}|\""
lowercase='abcdefghijklmnopqrstuvwxyz'
capital='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums='1234567890'
pwd=input()
flag_len=0
flag_num=0
flag_symbols=0
flag_lowercase=0
flag_capital=0
if len(pwd)>=8:
    flag_len=1
for ch in pwd:
    if ch in nums:
        flag_num=1
    elif ch in symbols:
        flag_symbols=1
    elif ch in lowercase:
        flag_lowercase=1
    elif ch in capital:
        flag_capital=1
n=flag_len+flag_lowercase+flag_num+flag_symbols+flag_capital
print(n)
