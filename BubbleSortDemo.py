list=[15,12,10,9,8,13]

for i in range(len(list)):
    print(i)

    for j in range(0,len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]


print(list)