def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    e=0
    while x>0:
        e+=1/x!
        x-=1
    print(e)

main()


