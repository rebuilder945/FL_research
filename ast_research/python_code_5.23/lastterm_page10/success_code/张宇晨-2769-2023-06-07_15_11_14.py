code=input()
mima=""
for x in code:
    if ord("a")-1< ord(x) < ord("z")+1:
        x=chr(97+ord("z")-ord(x))
        mima=mima+x
    elif ord("A")-1< ord(x) < ord("Z")+1:
        x=chr(65+ord("Z")-ord(x))
        mima=mima+x
    else:
        mima=mima+x
print(code)
print(mima)
