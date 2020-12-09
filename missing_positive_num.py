def segregate(arr, size): 
    j = 0
    for i in range(size): 
        if (arr[i] <= 0): 
            arr[i], arr[j] = arr[j], arr[i] 
            j += 1 # increment count of non-positive integers  
    return j  
  

def findMissingPositive(arr, size): 
      
    for i in range(size): 
        if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0): 
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

    print(arr)
              
    for i in range(size): 
        if (arr[i] > 0): 
              
            return i + 1
    return size + 1

def findMissing(arr, size): 
      
    return findMissingPositive(arr, size)  
      
arr = [ 1, 2, -4, -3, -5 ] 
arr_size = len(arr)  
missing = findMissing(arr, arr_size)  
print("The smallest positive missing number is ", missing) 