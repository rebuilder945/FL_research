def main():
    num = eval(input())
    calculate_e(num)
def calculat_e(num):
    e=1
    n=1
    for i in range(1,num+1):
        n=n*i
        e+=1/n
print("%.6f"%e)
    
main()


