
def search(n):
    for x in range(len(n)):
        if n.count(n[x])>int(n//2):
            a=n[x]
        else: 
            a="False"
    return a





nums = eval(input())
y = search(nums)
print(y)


