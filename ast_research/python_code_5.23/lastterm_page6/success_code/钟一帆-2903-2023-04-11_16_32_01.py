def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        e=1
        k=1
        for x in range(num):
                e+=1/k
                k*=(x+1)
        print(e)        
main()


