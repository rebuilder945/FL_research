def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(x):
        a=0
        b=1
        for i in range(x):
          if i == 0:
             
             a+=1
          else:
             b=b/i
             a+=b     
        print("%7f"%a)
              
              
main()


