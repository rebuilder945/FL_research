def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
      e=1
      a=1
      for i in range(1,int(num)+1):
            a=a*1/i
            e=e+a
      print('%.6f'%(e))
      
main()


