# a=input()
# m=0
# n=0
# b=0
# d=0
# for i in a:

    # if a.isalpha():
        # m+=1
    # elif a.isspace():
        #  n+=1
    # elif a.isdigit():
        #  b+=1
    # else:
        #  d+=1
# 
# print(m,n,b,d)

s=input('input a string:\n')
letters=0
space=0
digit=0
others=0
for c in s:
    if c.isalpha():
        letters+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        others+=1
print(letters,space,digit,others)
