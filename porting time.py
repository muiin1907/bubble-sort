import random
import time

def selection(listData):
    
    for outIter in range (len(listData)-1):
        
        minIndex=outIter
    
        for i in range (outIter+1,len(listData)):
            if listData[i]<listData[minIndex]:
                minIndex=i

        listData[outIter],listData[minIndex]=listData[minIndex],listData[outIter]

def modselection(listData):
    
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

    
        if cek :
            break
        
def random1000(listData):
    
    for i in range(1000):
        listData.append(random.randint(1,10000))
    print(len(listData))
    return(listData)   
    
listData=[]
#nge-random data
list1=random1000(listData)
list2=list1.copy()

mulai1=time.time()
selection(list1)
akhir1=time.time()
print('Algoritma selection sort konvensional :',(akhir1-mulai1))


mulai2=time.time()
modselection(list2)
akhir2=time.time()
print('Algoritma modifikasi selection sort :',(akhir2-mulai2))



