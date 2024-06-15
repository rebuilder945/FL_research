s=input()
mx,tmp="",""
for x in s:
    if x>='0' and x<='9':
        tmp+=x
    else:
        tmp=""
    if len(mx)<=len(tmp):
        mx=tmp
if mx=="":
    print("No digits")
else:
    print(mx)


