# basic array operations
basic_array = [1, 2, 3, 4, 5]
print("initial basic array:", basic_array)
print("accessing element at index 2:", basic_array[2]) 
basic_array[1] = 10
print("modify:", basic_array)
basic_array.append(6)
print("append:", basic_array)
basic_array.pop(1)
print("delete:", basic_array)

# traversing and sum
def array_sum(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum
arr_to_sum = [2, 4, 6, 8, 10]
print(arr_to_sum)
print("the sum of the array is:", array_sum(arr_to_sum))

# find max element
def find_max_element(arr):
  max = arr[0]
  for num in arr:
      if num > max:
          max = num
  return max  
arr_to_find_max = [1, 2, 3, 4, 5, 3, 4, 5, 2, 8, 7, 3, 2, 1]
print("max element of array is:", find_max_element(arr_to_find_max))
print("shortcut with max():", max(arr_to_find_max)) # shortcut!

# reversing an array
def reverse_array(arr):
  # two pointers (indices)
  start = 0
  end = len(arr) - 1

  while start < end:
    arr[start], arr[end] = arr[end], arr[start] # swapping
    start += 1
    end -= 1

before_reverse = [1, 2, 3, 4, 5]
print("original array: ", before_reverse)
reverse_array(before_reverse)
print("reversed an array:", before_reverse)

# remove duplicates from array 
def remove_duplicates(arr):
  unique = []
  for num in arr:
    if num not in unique: # -- not in -- keyword stored as boolean 
        unique.append(num)
  return unique  

contains_duplicates = [1, 2, 2, 3, 4, 4, 5, 5, 5, 8]
print("removed duplicates:", remove_duplicates(contains_duplicates))

# merge two arrays into one sorted array
def merge_arrays(a1, a2):
  merged = []
  i, j = 0, 0 
  while i < len(a1) and j < len(a2):
    if a1[i] < a2[j]:
      merged.append(a1[i])
      i += 1
    else:
      merged.append(a2[j])
      j += 1

  # leftover bits
  while i < len(a1):
    merged.append(a1[i])
    i += 1
  
  while j < len(a2):
    merged.append(a2[j])
    j += 1

  return merged      

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print("Merged array:", merge_arrays(arr1, arr2))         

# rotate an array to the right by k steps
def rotate_array(arr, k):
  # captures when k is greater than array length
  k = k % len(arr)
  return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
k = 2
print("Array rotated by 2 steps:", rotate_array(arr, k))

# binary search on sorted array
def binary_search(arr, target):
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left + right) // 2 # // returns only integer value of divison
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1 # no found 

sample = [1, 2, 3, 4, 5]
target = 4
print("Index of target 4:", binary_search(sample, target))