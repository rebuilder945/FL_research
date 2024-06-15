n=input()
for i in range(int(n)+1):
    if int(n[0])^2+int(n[1])^2+int(n[2])^2==int(n):
        print(i)
else:
    print('error')
