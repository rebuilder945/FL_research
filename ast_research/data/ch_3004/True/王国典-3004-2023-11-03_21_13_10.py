def find(Is):
    result=[]
    for i in range(len(Is)):
        if Is[i]%2!=0 and Is[i]%3!=0 and Is[i]%5!=0 and Is[i]!=1 and Is[i]%7!=0 or Is[i] in [2,3,5,7]:
            result.append(Is[i])
    return result
Is=eval(input())
print(find(Is))

