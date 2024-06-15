def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(k):
      e=0
      m=1
      for i in range(1,k+1):
            m=m/i
            e=e+m
      print("%.6f"%(e))
main()


