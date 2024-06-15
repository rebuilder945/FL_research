first=eval(input())
first.sort(reverse=True)
if len(first)==1 and int(first[0])==0:
        print("0")
else:
        for i in range(len(first)):
                print(first[i],end="")


