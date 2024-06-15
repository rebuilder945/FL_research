name = input()
score = input()
namelist = name.split(',')
# print(namelist)
score = score.lstrip('[')
score = score.rstrip(']')
scorelist = score.split(',')
# print(scorelist)
result=[]
for i in range(len(namelist)):
    result.append([namelist[i], int(scorelist[i])])
print(result)

#
# command = input()
# commandlist = command.split(',')
# num=int(commandlist[0])
# time=int(commandlist[1])
# step=int(commandlist[2])
# result = []
# for i in range(time):
#     result.append(num)
#     num += step
# print(result)



