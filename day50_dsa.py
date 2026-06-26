#Build Prefix Sum Array
def build_prefix_sum(arr):

    prefix = [0] * len(arr)

    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


arr = [2, 4, 6, 8, 10]

print("Original Array:", arr)
print("Prefix Sum:", build_prefix_sum(arr))


#Range Sum Query Using Prefix Sum
def range_sum(arr, left, right):

    prefix = [0] * len(arr)

    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    if left == 0:
        return prefix[right]

    return prefix[right] - prefix[left - 1]


arr = [10,20,30,40,50]

print(range_sum(arr, 1, 3))


#Multiple Range Queries
def multiple_queries(arr, queries):

    prefix = [0] * len(arr)

    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    for left, right in queries:

        if left == 0:
            print(prefix[right])
        else:
            print(prefix[right] - prefix[left - 1])


arr = [5,10,15,20,25]

queries = [
    (0,2),
    (1,4),
    (2,3)
]

multiple_queries(arr, queries)


#Range Sum Query - Immutable
class NumArray:

    def __init__(self, nums):

        self.prefix = [0] * len(nums)

        self.prefix[0] = nums[0]

        for i in range(1, len(nums)):
            self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, left, right):

        if left == 0:
            return self.prefix[right]

        return self.prefix[right] - self.prefix[left - 1]


nums = [1, 3, 5, 7, 9]

obj = NumArray(nums)

print(obj.sumRange(1, 3))
print(obj.sumRange(0, 4))
print(obj.sumRange(2, 4))