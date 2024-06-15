def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    c=[]
    b=1
    d=0
    for i in range(1,n+1):
        b=b*i
        d+=1/b
    print(d)
        
main()


