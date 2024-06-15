def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    x,s,b=0,0,0
    for i in range(a):
        
        s=s+a*10**x
        b=b+s
        x=x+1
    print(b)
main()

