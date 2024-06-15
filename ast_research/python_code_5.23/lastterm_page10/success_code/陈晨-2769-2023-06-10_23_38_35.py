m=(ord("a")+ord("z"))
M=(ord("B")+ord("Y"))
def f(s):
    if s.isupper():
        return chr(M-ord(s))
    else:
        return chr(m-ord(s))
    
string=input()
print(string)
for x in string:
    if x.isalpha():
        print(f(x),end="")
    else:
        print(x,end="")

