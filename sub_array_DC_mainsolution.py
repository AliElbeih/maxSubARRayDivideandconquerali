# better way to solve max subarray prob
def find_max_subarray(arr, low, high):
    # hena el basecase 
    if low == high:
        return [arr[low]]
    # to find midpoint to use for divde and conqour strategy either end or start of two seprate functions 
    mid = (low + high) // 2
    left = find_max_subarray(arr, low, mid)
    right = find_max_subarray(arr, mid + 1, high)
    #hena el unique case if the the subarray is in the between right and left of the midpoint 
    cross = find_max_crossing_subarray(arr, low, mid, high)
    return max(left, right, cross, key=lambda x: sum(x))

def find_max_crossing_subarray(arr, low, mid, high):
    left_sum, sum_, max_left = float('-inf'), 0, 0

    for i in range(mid, low - 1, -1):
        sum_ += arr[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i

    sum_, right_sum, max_right = 0, float('-inf'), 0

    for i in range(mid + 1, high + 1):
        sum_ += arr[i]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = i

    return arr[max_left:max_right + 1]

# Example usage
arr = [0,-2,3,4,-1,3,3,-1]
result = find_max_subarray(arr, 0, len(arr) - 1)
print(f"The maximum subarray is {result} with a sum of {sum(result)}")
#bigO(nlogn)