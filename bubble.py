def bubbleSort(listData):
    print('Data Awal',listData)
    for outIter in range (len(listData)-1,-1,-1):
        print(listData)
        for i in range (outIter):
            if listData[i]>listData[i+1]:
                listData[i],listData[i+1]=listData[i+1],listData[i]
    print('Data urut-',listData)

def modbubbleSort(listData):
    print('Data Awal',listData)
    
    for outIter in range(len(listData)-1,-1,-1):
        cek=True
        print(listData)
        for i in range (outIter):
            if listData[i]>listData[i+1]:
                listData[i],listData[i+1]=listData[i+1],listData[i]
            if i==(outIter-1):    
                for x in range (outIter-1,0,-1):
                    if listData[x]<listData[x-1]:
                        listData[x],listData[x-1]=listData[x-1],listData[x]
                        cek=False    
        if cek:
            break
    
    print('Data urut-',listData)

print('BUBBLE SORT')
a=[10,2,5,9,8,3,2,1]
bubbleSort(a)

print('MODIFIKASI BUBBLE SORT')
b=[10,2,5,9,8,3,2,1]
modbubbleSort(b)
