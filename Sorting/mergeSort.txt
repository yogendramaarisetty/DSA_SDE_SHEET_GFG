def merge_sort(arr):
    #array of length 1 is always sorted
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #recursion logic
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge logic
        i,j,k = 0,0,0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j] :
                arr[k] = left_arr[i]
                i+=1
            else :
                arr[k] = right_arr[j]
                j+=1
            k+=1

        #filling the remaining elements in arr
        while i<len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1
        

arr = [10,6,9,5,3,2,0,1]
merge_sort(arr)
print(arr)