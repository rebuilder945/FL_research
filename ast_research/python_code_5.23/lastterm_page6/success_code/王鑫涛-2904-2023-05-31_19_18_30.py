def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=0
    for i in range(a+1):
     
        c=str(a)*i
        if c!='':
            d=eval(c)
            b+=d
    print(b)
main()

