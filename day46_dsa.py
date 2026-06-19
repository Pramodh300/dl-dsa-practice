#Top K Largest Elements
import heapq

def top_k_largest(nums, k):
    return heapq.nlargest(k, nums)

nums = [3, 1, 5, 12, 2, 11]
k = 3

print("Top K Largest:", top_k_largest(nums, k))


#K Closest Numbers to X
import heapq

def k_closest(nums, x, k):
    heap = []

    for num in nums:
        distance = abs(num - x)
        heapq.heappush(heap, (distance, num))

    result = []

    for _ in range(k):
        result.append(heapq.heappop(heap)[1])

    return result

nums = [1, 2, 3, 4, 5]
x = 3
k = 2

print("K Closest Numbers:", k_closest(nums, x, k))



#Kth Largest Element in Array
import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

nums = [3, 2, 1, 5, 6, 4]
k = 2

print("Kth Largest:", kth_largest(nums, k))



#Merge K Sorted Lists
import heapq

def merge_k_sorted_lists(lists):
    heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []

    while heap:
        value, list_idx, element_idx = heapq.heappop(heap)

        result.append(value)

        next_idx = element_idx + 1

        if next_idx < len(lists[list_idx]):
            heapq.heappush(
                heap,
                (
                    lists[list_idx][next_idx],
                    list_idx,
                    next_idx
                )
            )

    return result

lists = [
    [1,4,5],
    [1,3,4],
    [2,6]
]

print("Merged List:", merge_k_sorted_lists(lists))