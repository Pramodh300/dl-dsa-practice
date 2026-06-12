#Longest Increasing Subsequence (LIS) + Print DP Array
def length_of_lis(nums):

    n = len(nums)

    # Step 1: Initialize DP array
    dp = [1] * n

    print("Initial DP:", dp)

    # Step 2: Build DP table
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

        print(f"After i = {i} (nums[{i}] = {nums[i]}): {dp}")

    print("\nFinal DP Array:", dp)
    print("Length of LIS:", max(dp))


nums = [10, 9, 2, 5, 3, 7, 101, 18]

print("===== TASK 6: LONGEST INCREASING SUBSEQUENCE =====")
print("Input Array:", nums)
length_of_lis(nums)


#LIS Dry Run Program (Print Table + Sequence)
def lis_with_sequence(nums):
    n = len(nums)

    dp = [1] * n
    parent = [-1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    # Find maximum LIS
    max_len = max(dp)
    index = dp.index(max_len)

    # Reconstruct sequence
    sequence = []
    while index != -1:
        sequence.append(nums[index])
        index = parent[index]

    sequence.reverse()

    # Print Table
    print("\nIndex\tValue\tdp[i]")
    for i in range(n):
        print(f"{i}\t{nums[i]}\t{dp[i]}")

    print("\nFinal DP Array :", dp)
    print("Length of LIS  :", max_len)
    print("One LIS Sequence:", sequence)


nums = [4, 10, 4, 3, 8, 9]

print("===== TASK 7: LIS DRY RUN =====")
print("Input:", nums)

lis_with_sequence(nums)