def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
    c=0
    for x in range(1,a+1):
        b=1
        for y in range(1,x+1):
            b=b*y
        c+=b
            
main()


