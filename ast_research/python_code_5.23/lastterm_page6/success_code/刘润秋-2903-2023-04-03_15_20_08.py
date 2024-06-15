def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
      e=1
      m=1
      for x in range(num):
            m*=(x+1)
            e+=1/m
      print("%.6f"%(e))
main()


