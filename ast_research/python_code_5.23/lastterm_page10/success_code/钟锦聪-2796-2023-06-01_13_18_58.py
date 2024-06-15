ls = input()
num =[]
for x in ls:
    if not "0"<=x<="9":
        print("No digits")
    else:
        for x in ls:
            if not "0"<=x<="9":
                num.append("0")
            else:
                num.append(x)
        str = "".join(num)
        ilist = []
        nem  =str.split("0")
        for x in nem:
            c = len(x)
            ilist.append(c)
        for x in nem[-1::]:
            if len(x)==max(ilist):
                print(int(x))
                break

