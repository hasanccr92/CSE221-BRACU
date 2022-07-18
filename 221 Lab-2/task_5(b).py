#-----------------TASK-5(b)-------------------


def findK(arr,low,high,k): #index+1 of the element
    if len(arr) == 0:
        return
    mid = low+high//2
    if mid == k-1:
        return arr[mid]
    
    if k-1<mid:
        return findK(arr,low,mid-1,k)
    return findK(arr,mid+1,high,k)
    
arr = [7, 5, 1, 9, 3, 11]
print(findK(arr,0,len(arr)-1,6))
