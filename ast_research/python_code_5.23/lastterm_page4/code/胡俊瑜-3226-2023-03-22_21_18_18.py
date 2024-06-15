def search(y):
      for x in y:
            if(y.count(x)>(lenth(y)/2)):
            return x;
            return False;





nums = eval(input())
y = search(nums)
print(y)


