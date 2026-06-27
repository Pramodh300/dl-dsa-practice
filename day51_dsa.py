#Next Greater Element
def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(nums[i])

    return result


nums = [2, 1, 2, 4, 3]
print(next_greater_element(nums))



#Daily Temperatures
def daily_temperatures(temperatures):
    stack = []
    answer = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            answer[index] = i - index

        stack.append(i)

    return answer


temps = [73,74,75,71,69,72,76,73]
print(daily_temperatures(temps))



#Stock Span Problem
def stock_span(prices):
    stack = []
    span = []

    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        if not stack:
            span.append(i + 1)
        else:
            span.append(i - stack[-1])

        stack.append(i)

    return span


prices = [100,80,60,70,60,75,85]
print(stock_span(prices))



#Largest Rectangle in Histogram
def largest_rectangle(heights):
    stack = []
    max_area = 0

    heights.append(0)

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            max_area = max(max_area, height * width)

        stack.append(i)

    heights.pop()

    return max_area


histogram = [2,1,5,6,2,3]
print(largest_rectangle(histogram))