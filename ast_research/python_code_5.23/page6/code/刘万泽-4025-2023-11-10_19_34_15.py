def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
       i=1
       a=[]
      while i<=num:
               if i==1:
                  b=1/i
                  a.append(b)
                  i+=1
               else:
                  i+=1
                  b=b*1/i
                  a.append(b)
    e=sum(a)+1
    print("%.6f"%e)
  
main()


