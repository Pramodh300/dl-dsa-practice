#Two Sum (LeetCode 1)
class Solution:

    def twoSum(self, nums, target):

        hashmap = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i

        return []


nums = [2, 7, 11, 15]
target = 9

obj = Solution()

result = obj.twoSum(nums, target)

print("Indices:", result)



#Valid Anagram(LeetCode 242)
class Solution:

    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        frequency = {}

        for ch in s:

            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

        for ch in t:

            if ch not in frequency:
                return False

            frequency[ch] -= 1

            if frequency[ch] < 0:
                return False

        return True


s = "anagram"
t = "nagaram"

obj = Solution()

print(obj.isAnagram(s, t))



#Contains Duplicate(LeetCode 217)
class Solution:

    def containsDuplicate(self, nums):

        seen = set()

        for num in nums:

            if num in seen:
                return True

            seen.add(num)

        return False


nums = [1, 2, 3, 4, 2]

obj = Solution()

print(obj.containsDuplicate(nums))



#Longest Substring Without Repeating Characters (LeetCode 3)
class Solution:

    def lengthOfLongestSubstring(self, s):

        hashmap = {}

        left = 0

        maximum = 0

        for right in range(len(s)):

            if s[right] in hashmap and hashmap[s[right]] >= left:

                left = hashmap[s[right]] + 1

            hashmap[s[right]] = right

            maximum = max(maximum, right - left + 1)

        return maximum


s = "abcabcbb"

obj = Solution()

print(obj.lengthOfLongestSubstring(s))


#Subarray Sum Equals K(LeetCode 560)
class Solution:

    def subarraySum(self, nums, k):

        prefix_sum = 0

        count = 0

        hashmap = {0: 1}

        for num in nums:

            prefix_sum += num

            if (prefix_sum - k) in hashmap:

                count += hashmap[prefix_sum - k]

            if prefix_sum in hashmap:

                hashmap[prefix_sum] += 1

            else:

                hashmap[prefix_sum] = 1

        return count


nums = [1, 1, 1]

k = 2

obj = Solution()

print(obj.subarraySum(nums, k))



#Group Anagrams(LeetCode 49)
from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs):

        groups = defaultdict(list)

        for word in strs:

            key = "".join(sorted(word))

            groups[key].append(word)

        return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

obj = Solution()

result = obj.groupAnagrams(words)

print(result)