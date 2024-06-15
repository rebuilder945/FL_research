def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
      e=1
     m=1
      for i in range(num):
            m*=(i+1)
      e+=1/m
      print(e)
main()


