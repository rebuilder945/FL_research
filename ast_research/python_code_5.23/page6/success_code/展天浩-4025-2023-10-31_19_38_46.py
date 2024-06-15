def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    e=0
    for i in range(1,x+1):
        d=1
        for j in range(1,x+1):
            d*=j
        e+=1/d 
    print(e)

main()


