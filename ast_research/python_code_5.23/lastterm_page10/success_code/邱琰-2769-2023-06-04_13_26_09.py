n=input()
nums=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ls=[i for i in n]
for i in range(len(ls)):
    if ls[i] in nums:
        icode=nums.index(ls[i])
        ls[i]=nums[26-icode]
print(n)
print(''.join(ls))
