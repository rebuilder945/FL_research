def main():
    a=int(input())
    calculate_sum(a)
def jia(n,m):
    x=0
    while m>0:
        x=n+x*10
        m-=1
    return x
def calculate_sum(num):
    c=0   
    for i in range(num):
        c+=jia(num,i+1)
    print(c)
       
main()

