def selection_sort(array):
    for i in range(len(array)):
        min_value_index=i
        for j in range(i+1,len(array)):
            if(array[j]<array[min_value_index]):
                min_value_index=j
        array[i],array[min_value_index]=array[min_value_index],array[i]
    
    return print(array)         
        
    

arr=[2, 3, 4, 10, 40, 36, 1, 54, 45, 5]

selection_sort(arr)