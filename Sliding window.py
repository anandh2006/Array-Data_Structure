🔰 What is the Sliding Window Technique?

The Sliding Window technique is a method used to reduce the time complexity of certain problems that involve arrays or strings — especially when you're working with contiguous subarrays or substrings.
Think of it like a window that you slide across the array to look at one part at a time — instead of recalculating everything from scratch each time.

🧱 Stage 1: Fixed Size Sliding Window (Basic)

    🔹 Useful when the window size is fixed (like "find max sum of subarray of size k")

🧪 Problem: Max sum of subarray of size k

Input: arr = [1, 2, 3, 4, 5, 6, 7], k = 3
Goal: Find maximum sum of any subarray of size 3
Naive approach: Recalculate sum for every group of 3 → O(n*k)

✅ Optimized with Sliding Window:

def max_sum_subarray(arr, k):
    n = len(arr)
    window_sum = sum(arr[:k])   # Initial window
    max_sum = window_sum

    for i in range(k, n):
        window_sum = window_sum - arr[i - k] + arr[i]  # Slide window
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [1, 2, 3, 4, 5, 6, 7]
print(max_sum_subarray(arr, 3))  # Output: 18
