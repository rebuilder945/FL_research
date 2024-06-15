def main():
    num = eval(input())
    calculate_e(num)
def calculat_e(num):
    e=1
    for i in range(1,num+1):
        for x in range(1,i):
            e+=1/i*1/x
print(e)
    
main()


