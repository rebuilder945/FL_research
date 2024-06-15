boy=int(input())
girl=int(input())
sum=boy+girl
bg=float(boy*100/sum)
gb=float(girl*100/sum)
bg=('%.2f'%(bg))
gb=('%.2f'%(gb))

# print(bg)
# print(type(bg))
print('The male students ratio is',bg,'%,the female students ratio is',gb,'%')
