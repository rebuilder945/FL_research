first=eval(input())
first.sort(reverse=True)
if int(sum(first))==0:
        print("0")
else:
        for i in range(len(first)):
                print(first[i],end="")


