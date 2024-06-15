def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
          s=1
          t=1
          for n in range(1,num+1):
              t*=n
              s+=(1/t)
          print("{:.6f}".format(s))
main()


