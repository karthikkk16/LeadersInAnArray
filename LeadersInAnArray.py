def leadersInAnArray(array):
    lead=[]
    maxi=-float('inf')
    for i in range(len(array)-1,-1,-1):
        if array[i]>maxi:
            maxi=array[i]
            lead.append(array[i])
    lead.reverse()
    return lead

array=list(map(int,input().split()))
print(leadersInAnArray(array))