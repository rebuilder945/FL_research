def calc(str):
    for x in str:
      if str.count(x)==1:
            return x
    return "None"

str=input()
print(calc(str))
