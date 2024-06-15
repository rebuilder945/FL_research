MonStr=input()
if MonStr[:3] in "RMB":
    U=(eval(MonStr[3:]))/6.78
    print("USD{:.2f}".format(U))
elif MonStr[:3] in "USB":
    R=(eval(MonStr[3:]))*6.78
    print("RMB{:.2f}".format(R))
elif MonStr[0] in "&":
    U=(eval(MonStr[1:]))/6.78
    print("${:.2f}".format(U))
elif MonStr[0] in "$":
    R=(eval(MonStr[1:]))*6.78
    print("&{:.2f}".format(R))
else:
    print("Error")
