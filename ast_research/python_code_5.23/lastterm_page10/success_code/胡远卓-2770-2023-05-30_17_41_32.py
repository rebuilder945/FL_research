def check(s1,s2):
      if len(s1)!=len(s2):
            return False
      for x in s1:
            if s1.count(x)!=s2.count(x):
                  return False
      return True

a=input()
b=input()
print(check(a,b))
