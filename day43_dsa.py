#Generate All Subsets (Power Set)
nums = [1, 2, 3]

result = []

def backtrack(index, current):
    # Store a copy of current subset
    result.append(current.copy())

    # Try adding each remaining element
    for i in range(index, len(nums)):
        current.append(nums[i])      # Choose
        backtrack(i + 1, current)    # Explore
        current.pop()                # Backtrack

backtrack(0, [])

print("All Subsets:")
for subset in result:
    print(subset)



#Generate All Permutations
nums = [1, 2, 3]

result = []
used = [False] * len(nums)

def backtrack(current):

    # If one complete permutation is formed
    if len(current) == len(nums):
        result.append(current.copy())
        return

    # Try every unused element
    for i in range(len(nums)):
        if used[i]:
            continue

        used[i] = True           # Choose
        current.append(nums[i])

        backtrack(current)       # Explore

        current.pop()            # Backtrack
        used[i] = False

backtrack([])

print("All Permutations:")
for perm in result:
    print(perm)



#Subsets of a String
s = "ABC"

result = []

def backtrack(index, current):
    result.append("".join(current))

    for i in range(index, len(s)):
        current.append(s[i])
        backtrack(i + 1, current)
        current.pop()

backtrack(0, [])

print("String Subsets:")
for item in result:
    print(item)



#Permutations of a String
s = "ABC"

result = []
used = [False] * len(s)

def backtrack(current):
    if len(current) == len(s):
        result.append("".join(current))
        return

    for i in range(len(s)):
        if used[i]:
            continue

        used[i] = True
        current.append(s[i])

        backtrack(current)

        current.pop()
        used[i] = False

backtrack([])

print("String Permutations:")
for item in result:
    print(item)