def MergeSort(array, l, r):

    if(len(array)==1):
        return array
    
    # divide the array into two parts

    avg = len(array)//2
    left = array[:avg]
    right = array[avg:]

    MergeSort(left, l, avg)
    MergeSort(right, avg+1, r)

    # To merge and sort two arrays into one main array
    def Merge(array, left, right):

        i = 0
        j = 0
        k = 0

        while(i < len(left) and j < len(right)):

            if(left[i] >= right[j]):
                array[k] = left[i]
                i += 1
                k += 1
            
            else:
                array[k] = right[j]
                j += 1
                k += 1
        
        # to insert remaining elements to the main array
        if(i < len(left)):
            while(i < len(left)):
                array[k] = left[i]
                i += 1
                k += 1
        
        else:
            while(j < len(left)):
                array[k] = right[j]
                j += 1
                k += 1
    
    Merge(array, left, right)   
    
array = [1,2,3,4]

MergeSort(array, 0, 3)

