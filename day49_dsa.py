#Maximum Sum Subarray of Size K
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right]
        window_sum -= arr[right - k]

        max_sum = max(max_sum, window_sum)

    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3

print(max_sum_subarray(arr, k))


#Smallest Subarray With Sum ≥ Target
def smallest_subarray(arr, target):

    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(arr)):

        current_sum += arr[right]

        while current_sum >= target:

            min_length = min(
                min_length,
                right - left + 1
            )

            current_sum -= arr[left]
            left += 1

    return min_length


arr = [2, 1, 5, 2, 3, 2]
target = 7

print(smallest_subarray(arr, target))



#Longest Substring Without Repeating Characters
def longest_unique_substring(s):

    left = 0
    seen = set()
    max_length = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        max_length = max(
            max_length,
            right - left + 1
        )

    return max_length


s = "abcabcbb"

print(longest_unique_substring(s))



#Maximum Consecutive Ones III
def longest_ones(nums, k):

    left = 0
    zeros = 0
    max_length = 0

    for right in range(len(nums)):

        if nums[right] == 0:
            zeros += 1

        while zeros > k:

            if nums[left] == 0:
                zeros -= 1

            left += 1

        max_length = max(
            max_length,
            right - left + 1
        )

    return max_length


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(longest_ones(nums, k))