def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
       x=[]
       for i in range(a+1):
            c=a+10**i
            x.append(c)
       s=sum(x)
       print(s)
main()

