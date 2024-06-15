def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num)：
      for x in range(0,10):
           e=1 
           n=1
           for i in range(1,1001+x*1000):
                     n=n+(1/i)
                     e+=n
           print("%.6f"%(e))

main()


