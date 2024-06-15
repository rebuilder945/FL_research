def main():
    num = eval(input())
    calculate_e(num)
def calculate_a(num):
      e=1
      for x in range(num):
           m=1
           for y in range(x+1):
                m*=y+1
           e+=1/m
       print('%.6f'%e)
main()


