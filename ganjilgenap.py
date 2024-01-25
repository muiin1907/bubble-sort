def ganjilgenapSort(listData):
    print('Data Awal= ',listData)
    for outIter in range (len(listData)):
        if(outIter%2==0):
            print('Genap-Ganjil Sorting')
            for i in range(0,len(listData)-1,2):
                if listData[i]>listData[i+1]:
                    listData[i],listData[i+1]=listData[i+1],listData[i]
            print(listData)
        else:
            print('Ganjil-Genap Sorting')
            for i in range(1,len(listData)-1,2):
                if listData[i]>listData[i+1]:
                    listData[i],listData[i+1]=listData[i+1],listData[i]
            print(listData)

    return listData
            
        
a=[13,12,10,8,7,5,11,2]
print(ganjilgenapSort(a))
