x = eval(input())
for i in range(x) :
    if i < 100 or i > 1000:
        pass
    else:
        if pow(int(str(i)[0]),3)+pow(int(str(i)[1]),3)+pow(int(str(i)[2]),3) == 100*int(str(i)[0])+10*int(str(i)[1])+int(str(i)[2]):
            print(i)
