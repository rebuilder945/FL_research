str1 = input()
li1 = list(map(int, str1[1:-1].split(',')))
num1 = len(li1)
for i in range(num1):
    for j in range(num1-i-1):
        if li1[j] < li1[j+1]:
            li1[j], li1[j+1] = li1[j+1], li1[j]
for i in range(num1):
    print(li1[i],end='')

