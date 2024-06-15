def count_foreign(ids):
    #20200001 20200002 L20190001 20200001
    count =0
    nums = list(map(str, input().split()))
    for i in nums:
        if i[0] == 'L':
            count +=1
    print(count)

origin=input().split()
print(count_foreign(origin))

