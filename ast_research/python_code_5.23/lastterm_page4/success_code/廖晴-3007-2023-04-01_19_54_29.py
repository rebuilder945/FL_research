s=eval(input())
n,m=eval(input())
if n>=len(s):
    print("error")
else:
    numbers=[i for i in range(len(s))]
    for x in numbers[n:m]:
        del s[x]
    print(s)
