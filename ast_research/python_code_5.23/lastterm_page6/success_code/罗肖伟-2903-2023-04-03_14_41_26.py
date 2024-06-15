def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
        e=1
        for i in range(1,x+1):
          t,m=1,1
          while t<=i:
           m*=t
           t+=1
        e+=1/m
        print("%.6f"%(e)) 

main()


