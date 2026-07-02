#Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

print(lengthOfLongestSubstring("abcabcbb"))


#Group Anagrams
from collections import defaultdict

def groupAnagrams(strs):
    mp = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        mp[key].append(word)

    return list(mp.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


#Product of Array Except Self
def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

print(productExceptSelf([1,2,3,4]))