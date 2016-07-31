def insertionSort(arr):
	for i in range(1,len(arr),1):
		key = arr[i]
		j = i-1
		while j >=0 and arr[j] > key:
			arr[j+1] = arr[j]
			j = j - 1
		arr[j + 1] = key	
	return arr 	   	

		
arr = [44,2,11,2,-3,2,11,123,0,109]
print ("The Unsorted array is")  
print (arr)
print ("========")
print ("The Sorted array is")
print (insertionSort(arr))


