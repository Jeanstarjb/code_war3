def find_even_index(arr):
    
    #for loop for iterating through 
    
    for i in range(len(arr)):
        
        #sum all numbers on left before the index
        left_sum = sum(arr[:i])
        
        #sum all numbers after the index
        right_sum = sum(arr[i+1:])
        
        #if condition for checking if left side is equal to right side
        if left_sum == right_sum:
            
            return i
        
    return -1
