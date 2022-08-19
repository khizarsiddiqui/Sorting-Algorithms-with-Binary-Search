# Optimized Bubble sort in Python

def bubbleSort(array):
    
  # loop through each element of array
  for i in range(len(array)):
        
    # keep track of swapping
    swapped = False
    
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping occurs if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        swapped = True
          
    # no swapping means the array is already sorted
    if not swapped:
      break

data = [5, 12, 10, 1, 3]

print('Array before bubble sort:')
print(data)
bubbleSort(data)
print('Sorted Array in Ascending Order using bubble sort:')
print(data)

# def bubblesort(elements):
# 	swapped = False
# 	# Looping from size of array from last index[-1] to index [0]
# 	for n in range(len(elements)-1, 0, -1):
# 		for i in range(n):
# 			if elements[i] > elements[i + 1]:
# 				swapped = True
# 				# swapping data if the element is less than next element in the array
# 				elements[i], elements[i + 1] = elements[i + 1], elements[i]	
# 		if not swapped:
# 			# exiting  if  the array is already sorted.
# 			return

# elements = [5, 12, 10, 1, 3]

# print("Unsorted array:")
# print(elements)
# bubblesort(elements)
# print("Sorted Array using bubble sort:")
# print(elements)
