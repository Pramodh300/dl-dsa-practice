#Group Anagrams
from collections import defaultdict

def groupAnagrams(strs):

    groups = defaultdict(list)

    for word in strs:

        key = "".join(sorted(word))

        groups[key].append(word)

    return list(groups.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))



#Top K Frequent Elements
from collections import Counter

def topKFrequent(nums, k):

    frequency = Counter(nums)

    sorted_items = sorted(
        frequency.items(),
        key=lambda x: x[1],
        reverse=True
    )

    answer = []

    for num, freq in sorted_items[:k]:
        answer.append(num)

    return answer


nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums, k))



#Search in Rotated Sorted Array
def search(nums, target):

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

print(search(nums, target))



#Number of Islands
def dfs(grid, r, c):

    rows = len(grid)
    cols = len(grid[0])

    if r < 0 or c < 0 or r >= rows or c >= cols:
        return

    if grid[r][c] == "0":
        return

    grid[r][c] = "0"

    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)


def numIslands(grid):

    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):

            if grid[r][c] == "1":

                count += 1
                dfs(grid, r, c)

    return count


grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

print(numIslands(grid))