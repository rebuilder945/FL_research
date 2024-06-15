def grade(str):
      F1,F2,F3,F5=0,0,0,0
      for x in str:
            if x>='0' and x<='9':
                  F1=1
            elif x>='a' and x<='z':
                  F2=1
            elif x>='A' and x<='Z':
                  F3=1
            elif x in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\":
                  F5=1
      F4=int(len(str)>=8)
      return F1+F2+F3+F4+F5

str=input()
print(grade(str))
