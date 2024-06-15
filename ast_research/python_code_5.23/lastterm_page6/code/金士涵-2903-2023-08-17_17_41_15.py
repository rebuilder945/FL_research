def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
      n=1
      e=1
      for i range(0,num+1):
             e=e+1/n*i
             print(e)
main()


