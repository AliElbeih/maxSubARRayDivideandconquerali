
# el clasic way to solve max subarray prob 
def max_subarray_bruteforce(arr):
    n = len(arr)

    if n == 0:
        return []

    max_sum = float('-inf')
    max_sub = []

    for i in range(n):
        cur_sum = 0
        for k in range(i, n):
            cur_sum += arr[k]
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_sub = arr[i:k + 1]

    return max_sub

# Example usage
arr = [0,-2,3,4,-1,3,3,-1]
result = max_subarray_bruteforce(arr)
print(f"The maximum subarray is {result} with a sum of {sum(result)}")

#bigO(n^2)
