#Koko Eating Bananas(Binary Search on Answer)
import math

def minEatingSpeed(piles, h):

    left = 1
    right = max(piles)

    while left < right:

        mid = (left + right) // 2

        hours = 0

        for pile in piles:
            hours += math.ceil(pile / mid)

        if hours <= h:
            right = mid
        else:
            left = mid + 1

    return left


piles = [3,6,7,11]
h = 8

print(minEatingSpeed(piles, h))


#Longest Repeating Charactrer Replacement (Sliding Window)
def characterReplacement(s, k):

    count = {}

    left = 0

    max_freq = 0

    answer = 0

    for right in range(len(s)):

        count[s[right]] = count.get(s[right], 0) + 1

        max_freq = max(max_freq, count[s[right]])

        while (right - left + 1) - max_freq > k:

            count[s[left]] -= 1
            left += 1

        answer = max(answer, right - left + 1)

    return answer


print(characterReplacement("AABABBA",1))



#Number of Islands (DFS)
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
    ["1","1","0","0"],
    ["1","0","0","1"],
    ["0","0","1","1"],
    ["1","0","0","0"]
]

print(numIslands(grid))



#Capacity To Ship Packages Within D Days (LeetCode 1011)
def shipWithinDays(weights, days):

    left = max(weights)
    right = sum(weights)

    while left < right:

        mid = (left + right) // 2

        required_days = 1
        current_weight = 0

        for weight in weights:

            if current_weight + weight > mid:
                required_days += 1
                current_weight = 0

            current_weight += weight

        if required_days <= days:
            right = mid
        else:
            left = mid + 1

    return left


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(shipWithinDays(weights, days))