def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(x):
        a=1
        b=1
        for i in range(x):
          b=b/i
          a+=b     
              
              
main()


