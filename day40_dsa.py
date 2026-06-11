#LCS Length (Basic DP)
def longest_common_subsequence(text1, text2):
    m = len(text1)
    n = len(text2)

    # DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


text1 = "abcde"
text2 = "ace"

print("LCS Length:", longest_common_subsequence(text1, text2))



#Print the Actual LCS String
def print_lcs(text1, text2):
    m, n = len(text1), len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to build LCS string
    i, j = m, n
    lcs = []

    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs))


text1 = "abcde"
text2 = "ace"

print("LCS:", print_lcs(text1, text2))


#Recursive LCS
def lcs_recursive(text1, text2, m, n):

    # Base case
    if m == 0 or n == 0:
        return 0

    # Characters match
    if text1[m - 1] == text2[n - 1]:
        return 1 + lcs_recursive(text1, text2, m - 1, n - 1)

    # Characters don't match
    return max(
        lcs_recursive(text1, text2, m - 1, n),
        lcs_recursive(text1, text2, m, n - 1)
    )


text1 = "abcde"
text2 = "ace"

print("LCS Length:", lcs_recursive(text1, text2, len(text1), len(text2)))


#LCS with Memoization
def lcs_memo(text1, text2):
    memo = {}

    def solve(i, j):
        # Base case
        if i == len(text1) or j == len(text2):
            return 0

        # Already computed
        if (i, j) in memo:
            return memo[(i, j)]

        # Characters match
        if text1[i] == text2[j]:
            memo[(i, j)] = 1 + solve(i + 1, j + 1)
        else:
            memo[(i, j)] = max(
                solve(i + 1, j),
                solve(i, j + 1)
            )

        return memo[(i, j)]

    return solve(0, 0)


text1 = "abcde"
text2 = "ace"

print("LCS Length:", lcs_memo(text1, text2))