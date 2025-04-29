def selc(arr):
    arr=[]
    a=len(arr)
    for i in range (a):
        s=i
        for j in range (i+1,a):
            if arr[j]<arr[s]:
                s=j
                s,j=j,s
    return arr
arr=[5, 2, 9, 1, 5, 6]        
selc(arr)
print("Sorted array:", arr)
