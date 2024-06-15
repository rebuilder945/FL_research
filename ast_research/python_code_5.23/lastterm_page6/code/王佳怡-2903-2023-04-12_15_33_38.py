def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    for i in range(1,num+1):
        e=1
        e+=1/i!
    print("%.6f" %(e))
  
main()


