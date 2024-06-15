def calc(str):
    tmp=""
    for x in str:
      if x>='A' and x<='Z':
            tmp+=chr(25-ord(x)+2*ord('A'))
      elif x>='a' and x<='z':
            tmp+=chr(25-ord(x)+2*ord('a'))
      else:
           tmp+=x
    return tmp

str=input()
print(str)
print(calc(str))
