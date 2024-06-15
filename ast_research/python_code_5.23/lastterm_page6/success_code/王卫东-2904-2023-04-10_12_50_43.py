def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b = 0
    for x in range(1,a+1):
        c=0
        for y in range(1,x+1):
            c=c*10+a
        b = b+c    
    print(b) 
main()

