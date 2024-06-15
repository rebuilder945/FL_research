names = input().split(',')#tom,jack,jone,mike
a = eval(input())#[88,89,34,90]     [['tom', 88], ['jack', 89], ['jone', 34], ['mike', 90]]
b = []
for x in range(len(a)):
    b.append([names[x],a[x]])
print(b)

