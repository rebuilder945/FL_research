def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num): 
      e=1
      for i in range(num):
           m=1
           for y in range(i+1):
                m^i=y+1
                e+=1/m
      print("%.6f"%(e))

main()


