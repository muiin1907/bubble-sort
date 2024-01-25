def selection(listData):
    
    print('data awal',listData)
    
    for outIter in range (len(listData)-1):
        
        minIndex=outIter
    
        for i in range (outIter+1,len(listData)):
            if listData[i]<listData[minIndex]:
                minIndex=i

        listData[outIter],listData[minIndex]=listData[minIndex],listData[outIter]
        
        print(listData)
        
    print('data urut-',listData)

def modselection(listData):
    
    print('data awal',listData)
    
    for outIter in range (len(listData)-1):
        cek=True
        minIndex=outIter
        maxIndex=((len(listData)-1)-outIter)
        
        for i in range (outIter+1,len(listData)):
            if listData[i]<listData[minIndex]:
                minIndex=i
                cek=False
        listData[outIter],listData[minIndex]=listData[minIndex],listData[outIter]
        
        for i in range (outIter+1,len(listData)):
            if listData[(len(listData)-1)-i]>listData[maxIndex]:
                maxIndex=(len(listData)-1)-i
                cek=False

        listData[(len(listData)-1)-outIter],listData[maxIndex]=listData[maxIndex],listData[(len(listData)-1)-outIter]        

        print(listData)
        if cek :
            break
        
    print('data urut-',listData)
    
a=[10,2,5,8,1,3,15,4,20,8,12,6,9,100,2,101]
print('SELECTION SORT')
selection(a)

b=[10,2,5,8,1,3,15,4,20,8,12,6,9,100,2,101]
print('MODIFIKASI SELECTION SORT')
modselection(b)
