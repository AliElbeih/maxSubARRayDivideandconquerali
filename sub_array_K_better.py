def find_max_subarray_kadane(arr):
    max_sum = float('-inf')
    current_sum = 0
    start_index = 0
    end_index = 0
    current_start_index = 0
    for i, num in enumerate(arr):
        if num > current_sum + num:
            current_sum = num
            current_start_index = i
        else:
            current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = current_start_index
            end_index = i
    max_subarray = arr[start_index:end_index + 1]
    return max_sum, max_subarray
# Example usage
arr = [-1,-2,6,-4,2,3,2,-1]
result_sum, result_subarray = find_max_subarray_kadane(arr)
print(f"The maximum subarray sum is {result_sum}")
print(f"The maximum subarray is {result_subarray}")
#big O(n)