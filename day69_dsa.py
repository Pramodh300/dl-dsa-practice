#Two Sum (Easy)
class Solution:

    def twoSum(self, nums, target):

        hashmap = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9

obj = Solution()

print(obj.twoSum(nums, target))


#Maximum Depth of Binary Tree(Easy)
class TreeNode:

    def __init__(self, val=0):

        self.val = val
        self.left = None
        self.right = None


class Solution:

    def maxDepth(self, root):

        if root is None:
            return 0

        left = self.maxDepth(root.left)

        right = self.maxDepth(root.right)

        return max(left, right) + 1


root = TreeNode(3)

root.left = TreeNode(9)

root.right = TreeNode(20)

root.right.left = TreeNode(15)

root.right.right = TreeNode(7)

obj = Solution()

print(obj.maxDepth(root))



#Search in Rotated Sorted Array(Medium)
class Solution:

    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:

                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


nums = [4,5,6,7,0,1,2]

target = 0

obj = Solution()

print(obj.search(nums, target))



#Longest Substring Without Repeating Characters(Medium)
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