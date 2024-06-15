list = eval(input())
ave = sum(list)/len(list)
if ave == int(ave):
    ave = int(ave)
    print(ave)
else:
    print("%.2f"%ave)
