str_input = raw_input()
str_list = []
str_o = ''
str_input_add = str_input + " "
for i in str_input_add:
    if i.isdigit():
        str_o = str_o + i
    else:
        if str_o:
            str_list.append(str_o)
        str_o = ''
        continue
print str_list
 
if not str_list:
    print ""
else:
    res = str_list[0]
    for j in str_list:
        if len(j) >= len(res):
            res = j
        else:
            pass
    print res, len(res)
