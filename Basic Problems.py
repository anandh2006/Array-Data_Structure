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

        
    
