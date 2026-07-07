#Amazon Pattern 1 — Top K / K Closest (Heap)
import heapq
from collections import Counter

def topKFrequent(words, k):
    freq = Counter(words)

    # Min-heap of size k
    # Store (-frequency, word) — negative so higher freq = smaller (min-heap pops smallest)
    # For same frequency: Python compares strings lexicographically
    heap = []

    for word, count in freq.items():
        heapq.heappush(heap, (-count, word))

    return [heapq.heappop(heap)[1] for _ in range(k)]

# Test
print(topKFrequent(["i","love","leetcode","i","love","coding"], 2))
# ["i","love"]

print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))
# ["the","is","sunny","day"]


#Amazon Pattern 2 — LRU Cache (LeetCode 146)
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()   # key → value, ordered by recency

    def get(self, key):
        if key not in self.cache:
            return -1

        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)   # update recency
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # remove LEAST recently used (front)

# Test
cache = LRUCache(2)
cache.put(1, 1)    # cache: {1:1}
cache.put(2, 2)    # cache: {1:1, 2:2}
print(cache.get(1))  # 1 — cache: {2:2, 1:1}  (1 moved to end)
cache.put(3, 3)    # evict 2 (LRU) — cache: {1:1, 3:3}
print(cache.get(2))  # -1 (evicted)
print(cache.get(3))  # 3


#Amazon Pattern 3 — Trapping Rain Water / Stock Problems (Array)
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price              # found cheaper buy point
        elif price - min_price > max_profit:
            max_profit = price - min_price # found better profit

    return max_profit

print(maxProfit([7,1,5,3,6,4]))   # 5  (buy at 1, sell at 6)
print(maxProfit([7,6,4,3,1]))     # 0  (prices only drop)


#Amazon Pattern 4 — Number of Islands / Connected Components (Graph BFS/DFS)
def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        # Out of bounds or water or already visited
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'   # mark visited (sink the island)
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)   # sink the entire island

    return count

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(numIslands(grid))   # 3


#Flipkart Pattern 1 — Meeting Rooms / Interval Problems
import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])   # sort by start time
    end_times = []   # min-heap of end times

    for start, end in intervals:
        # If earliest ending meeting ended before this starts
        if end_times and end_times[0] <= start:
            heapq.heappop(end_times)   # reuse that room

        heapq.heappush(end_times, end)   # assign room

    return len(end_times)   # rooms in use = answer

print(minMeetingRooms([[0,30],[5,10],[15,20]]))   # 2
print(minMeetingRooms([[7,10],[2,4]]))             # 1



#Flipkart Pattern 2 — Product Search (Tries)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Test — search autocomplete
trie = Trie()
for word in ["apple", "app", "application", "apply", "apt"]:
    trie.insert(word)

print(trie.search("app"))        # True
print(trie.search("ap"))         # False (not inserted as complete word)
print(trie.startsWith("app"))    # True (prefix exists)
print(trie.startsWith("xyz"))    # False



# Flipkart Pattern 3 — Discount/Greedy Problems
def canJump(nums):
    max_reach = 0   # farthest index reachable so far

    for i, jump in enumerate(nums):
        if i > max_reach:
            return False           # can't even reach this position
        max_reach = max(max_reach, i + jump)

    return True

print(canJump([2,3,1,1,4]))   # True
print(canJump([3,2,1,0,4]))   # False (stuck at index 3)