ha = input()
if ha[0] == str($) or ha[0:2] == USD:
    c = eval(ha)/6.78
    if ha[0] == str($):
        print("&%.2f"%c)
    else:
        print("RMB%.2F"%c)
elif ha[0] == & or ha[0:2] == RMB:
    c = eval(ha)*6.78
    if ha[0] == &:
        print("$%.2f"%c)
    else:
        print("USD%.2f"%c)
else:
    print("error")
