#Create a Min Heap and Insert Elements
import heapq

nums = []

heapq.heappush(nums, 5)
heapq.heappush(nums, 3)
heapq.heappush(nums, 8)
heapq.heappush(nums, 1)

print("Min Heap:", nums)
print("Smallest Element:", nums[0])


#Remove Elements from Min Heap
import heapq

nums = [5, 3, 8, 1]

heapq.heapify(nums)

while nums:
    print(heapq.heappop(nums))



#Create a Max Heap
import heapq

nums = [5, 3, 8, 1]

max_heap = [-x for x in nums]

heapq.heapify(max_heap)

print("Largest Element:", -max_heap[0])

while max_heap:
    print(-heapq.heappop(max_heap))



#Find K Largest Elements
import heapq

nums = [10, 4, 15, 7, 20, 3]

k = 3

result = heapq.nlargest(k, nums)

print("K Largest Elements:", result)