#Two Sum(HashMap Pattern)
def two_sum(nums, target):

    hashmap = {}

    for i in range(len(nums)):

        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))


#Best Time to Buy and Sell Stock(Array Pattern)
def max_profit(prices):

    min_price = float('inf')
    max_profit = 0

    for price in prices:

        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


prices = [7, 1, 5, 3, 6, 4]

print(max_profit(prices))



#Valid Parentheses(Stack Pattern)
def is_valid(s):

    stack = []

    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:

        if ch in "([{":
            stack.append(ch)

        else:

            if not stack:
                return False

            top = stack.pop()

            if mapping[ch] != top:
                return False

    return len(stack) == 0


print(is_valid("{[()]}"))
print(is_valid("{[(])}"))



#Binary Search (Google Favorite)
def binary_search(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


nums = [2, 4, 6, 8, 10]

print(binary_search(nums, 8))