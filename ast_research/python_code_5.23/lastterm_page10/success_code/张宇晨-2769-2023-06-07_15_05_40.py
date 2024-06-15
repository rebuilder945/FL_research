code=input()
mima=""
for x in code:
    if x.isalpha():
        x=chr(97+ord("z")-ord(x))
        mima=mima+x
    else:
        mima=mima+x
print(mima)
print(code)
