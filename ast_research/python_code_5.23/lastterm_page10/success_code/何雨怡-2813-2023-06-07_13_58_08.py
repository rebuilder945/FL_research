s=input()
sub=input()
while sub in s:
    s=s.replace(sub,"")
print(s)
