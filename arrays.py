# basic array operations
array = [1, 2, 3, 4, 5]
print("initial:", array)
print("access:", array[2]) 
array[1] = 10
print("modify:", array)
array.append(6)
print("append:", array)
array.pop(1)
print("delete:", array)

# traversing and sum
def array_sum(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum
arr = [1, 2, 3, 4, 5]
print(arr)
print("array sum:", array_sum(arr))

# find max element
def find_max_element(arr):
  max = arr[0]
  for num in arr:
      if num > max:
          max = num
  return max  

print("max element of array is:", find_max_element(arr))
print(max(arr)) # shortcut!

# reversing an array
def reverse_array(arr):
  # two pointers (indices)
  start = 0
  end = len(arr) - 1

  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print("reversed an array:", arr)

# remove duplicates from array 
def remove_duplicates(arr):
  unique = []
  for num in arr:
    if num not in unique: # -- not in -- keyword stored as boolean 
        unique.append(num)
  return unique  

arr = [1, 2, 2, 3, 4, 4, 5, 5, 5, 8]
print("removed duplicates:", remove_duplicates(arr))

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

arr = [1, 2, 3, 4, 5]
target = 4
print("Index of target 4:", binary_search(arr, target))