def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    for i in range(1,num+1):      
        b=1
        for x in range(i):
            b*=x
        e+=1/b
    print("%.6f" %(e))
  
main()


