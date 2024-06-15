def find_prime(nums):
 result=[]
 for num in nums:
    if num > 1:
      for i in range(2,num):
          if (num % i) == 0:
              break
      else:
          result.append(num)
    else:
      pass
 return result
list=eval(input())
a=find_prime(list)
print(a)


