def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
      e=0
      while num-1>0:
                 a=num
                 for i in range(1,num):
                       a=a*i
                 return a
                 e+=1/a
main()


