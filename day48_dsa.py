#Three Sum
def threeSum(nums):
    nums.sort()     # MUST sort first
    result = []

    for i in range(len(nums) - 2):

        # Skip duplicates for the fixed element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1    # need bigger sum
            else:
                right -= 1   # need smaller sum

    return result

# Test
print(threeSum([-1, 0, 1, 2, -1, -4]))
# [[-1, -1, 2], [-1, 0, 1]]

print(threeSum([0, 0, 0]))
# [[0, 0, 0]]



# Container With Most Water 
def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # Current container's water
        water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, water)

        # Move the SHORTER pointer (greedy choice)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Test
print(maxArea([1,8,6,2,5,4,8,3,7]))   # 49
print(maxArea([1,1]))                   # 1



#Remove Duplicates from Sorted Array
def removeDuplicates(nums):
    if not nums:
        return 0

    slow = 0   # points to last unique element written

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:   # found a new unique element
            slow += 1
            nums[slow] = nums[fast]    # write it

    return slow + 1   # length of unique portion

# Test
nums = [1, 1, 2, 3, 3, 4]
k = removeDuplicates(nums)
print(nums[:k])   # [1, 2, 3, 4]



#Trapping Rain Water 
def trap(height):
    left, right = 0, len(height) - 1
    max_left = max_right = 0
    water = 0

    while left < right:
        if height[left] <= height[right]:
            if height[left] >= max_left:
                max_left = height[left]   # new max on left
            else:
                water += max_left - height[left]   # trapped water
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                water += max_right - height[right]
            right -= 1

    return water

# Test
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6
print(trap([4,2,0,3,2,5]))                 # 9



#Fast & Slow Pointers (Floyd's Cycle Detection)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next         # moves 1 step
        fast = fast.next.next    # moves 2 steps

        if slow == fast:         # they met → cycle exists
            return True

    return False   # fast reached end → no cycle