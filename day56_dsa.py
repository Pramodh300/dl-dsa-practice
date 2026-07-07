#Kadane’s Algorithm
def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


#Longest Repeating Character Replacement
from collections import defaultdict

def characterReplacement(s, k):
    count = defaultdict(int)
    left = 0
    max_freq = 0
    result = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])

        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


print(characterReplacement("AABABBA", 1))



#Subarray Sum Equals K
def subarraySum(nums, k):
    prefix_sum = 0
    count = {0: 1}
    result = 0

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in count:
            result += count[prefix_sum - k]

        count[prefix_sum] = count.get(prefix_sum, 0) + 1

    return result


print(subarraySum([1,1,1], 2))