s = input()
s_del = input()
if s_del in s:
    s0 = s.replace(s_del,'')
else:
    s0 = s
print(s0)
