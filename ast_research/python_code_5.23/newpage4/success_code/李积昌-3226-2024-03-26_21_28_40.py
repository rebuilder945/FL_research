def search(a) :
        n=len(a)
        for x in a :
            b=a.count(x)
            if b > n //2 :
                return x
        return False





nums = eval(input())
y = search(nums)
print(y)


