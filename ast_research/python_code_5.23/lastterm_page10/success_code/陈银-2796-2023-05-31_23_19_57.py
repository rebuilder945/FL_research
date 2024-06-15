s = input()
max_num = ""
curr_num = ""
for i in range(len(s)):
    if s[i].isdigit():
        curr_num += s[i]
    else:
        if len(curr_num) >= len(max_num):
            max_num = curr_num
        curr_num = ""
if len(curr_num) >= len(max_num):
    max_num = curr_num
if max_num:
    print(max_num)
else:
    print( "No digits")


