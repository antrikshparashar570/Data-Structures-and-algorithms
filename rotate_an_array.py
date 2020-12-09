def leftRotate(A, d, n): 
    d = d % n 
    g_c_d = gcd(d, n) 
    for i in range(g_c_d): 
        temp = A[i]
        j = i
        while 1:
            k = j+d
            if k >= n:
                k = k-n
            if k == i:
                break
            A[j] = A[k]
            j = k
        A[j] = temp
  
# UTILITY FUNCTIONS 
# function to print an array  
def printArray(arr, size): 
    for i in range(size): 
        print ("% d" % arr[i], end =" ") 
  
# Fuction to get gcd of a and b 
def gcd(a, b): 
    if b == 0: 
        return a; 
    else: 
        return gcd(b, a % b) 
  
# Driver program to test above functions  
arr = [1, 2, 3, 4, 5, 6, 7] 
n = len(arr) 
d = 3
leftRotate(arr, d, n) 
printArray(arr, n)