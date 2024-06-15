lt=input()
lt1=list(lt.split(','))
lt2=eval(input())
lt3=[[lt1[n],lt2[n]]for n in range(len(lt1))]
print(lt3)
