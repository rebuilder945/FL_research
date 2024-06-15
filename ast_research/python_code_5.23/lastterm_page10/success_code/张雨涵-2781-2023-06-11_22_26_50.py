def convert_char(ch):
    if ch>="a" and ch<="z":
        ch=ch.upper()
    elif ch>="A" and ch<="Z":
        ch=ch.lower()
        return ch
with open("data.txt","r") as f:
    while True:
        ch=f.read(1)
        res=convert_char(ch)
        print(res,end="")
        if not ch:
            break
