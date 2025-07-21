Find maximum in an Array:

arr = [1,9,3,4,5]
max = arr[0]
for i in range(1,len(arr)):
    if arr[i] > max:
        max = arr[i]
print(max)
        
    (or)

print(max(arr))

Find minimum in an Array:

arr = [10,9,3,4,16]
min = arr[0]
for i in range(1,len(arr)):
    if arr[i] < min:
        min = arr[i]
print(min)

(or)

print(min(arr))

Sum and Average

arr = [1,2,3,4,5]
sum = 0
for i in range(len(arr)):
    sum += arr[i]
    
print("Sum :",sum)
print("Average :",sum // len(arr))

Reverse the Array:

arr = [1, 2, 3, 4, 5]
print(arr[::-1])  
    (or)
print(list(reversed(arr)))  

Check the array is sorted or not:

arr = [4, 3, 5, 2, 7]

is_sorted = True
for i in range(1, len(arr)):
    if arr[i-1] > arr[i]:
        is_sorted = False
        break

if is_sorted:
    print("Sorted in increasing order")
else:
    print("Not sorted")

Count even and odd numbers

arr = [1,2,3,4,5]
even = 0
odd = 0
for i in range (len(arr)):
    if arr[i]%2 == 0:
        even += 1
    else:
        odd += 1
print(even)
print(odd)

Second largest element in an array

def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None
arr = [3, 5, 1, 9, 7]
print("Second largest:", second_largest(arr))

(or)

def second_largest(arr):
    unique = list(set(arr))
    if len(unique) < 2:
        return None
    unique.sort(reverse=True)
    return unique[1]

Left Rotate by 1 or d position

Left Rotate by 1 Position

def rotate_left_by_one(arr):
    if len(arr) == 0:
        return arr
    first = arr.pop(0)
    arr.append(first)
    return arr

arr = [1, 2, 3, 4, 5]
rotated = rotate_left_by_one(arr)
print(rotated)

Left Rotate by d Position    

def rotate_left_by_d(arr, d):
    n = len(arr)
    d = d % n  
    return arr[d:] + arr[:d]

arr = [1, 2, 3, 4, 5]
d = 2
rotated = rotate_left_by_d(arr, d)
print(rotated)

Right Rotate by 1

def right_rotate_by_1(arr):
    last = arr.pop()      
    arr.insert(0, last)   
    return arr

arr = [1, 2, 3, 4, 5]
print("After 1 right rotate:", right_rotate_by_1(arr))

Right Rotate by d Positions

def right_rotate(arr, d):
    n = len(arr)
    d = d % n  
    return arr[-d:] + arr[:-d]


arr = [1, 2, 3, 4, 5]
d = 2
rotated = right_rotate(arr, d)
print("After right rotate:", rotated)


