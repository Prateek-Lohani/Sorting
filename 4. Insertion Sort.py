def insertion_sort(arr):
    length=len(arr)
    for i in range(1,length):
        j=i-1
        temp=arr[i]
        while(j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp    
    return print(arr)
    
    
arr=[5,7,6,4,1,23,2,3,14]    
insertion_sort(arr) 