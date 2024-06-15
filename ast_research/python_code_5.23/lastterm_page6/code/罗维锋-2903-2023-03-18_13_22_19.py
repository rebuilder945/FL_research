def main():
    num = eval(input())
    calculate_e(num)
def  nen(a):
       s=1
       for i in range(1,a+1):
           s*=i
       return s
def  calculate_e(n):
       e=1
       i=1
       while i<=n:
           e+=1/nen(i)
           i+=1
        print("{:.6f}.format(e))
        
main()


