def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(k):
      e=0
      m=1
      for i in range(k):
            m=m/i
            e=e+m
      print(e)
main()


