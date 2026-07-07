#House Robber (Pick/Not Pick DP)
def houseRobber(nums):

    n = len(nums)


    if n == 1:
        return nums[0]


    dp = [0] * n


    dp[0] = nums[0]


    dp[1] = max(
        nums[0],
        nums[1]
    )


    for i in range(2,n):

        pick = nums[i] + dp[i-2]

        skip = dp[i-1]


        dp[i] = max(
            pick,
            skip
        )


    return dp[-1]



houses = [2,7,9,3,1]


print(
    houseRobber(houses)
)


#Coin Change (Minimum Coins)
def coinChange(coins, amount):


    dp = [float('inf')] * (amount+1)


    dp[0] = 0



    for value in range(
        1,
        amount+1
    ):


        for coin in coins:


            if value >= coin:


                dp[value] = min(

                    dp[value],

                    1 + dp[value-coin]

                )



    if dp[amount] == float('inf'):

        return -1


    return dp[amount]





coins = [1,2,5]

amount = 11


print(
    coinChange(
        coins,
        amount
    )
)



#Longest Increasing Subsequence (LIS)
def LIS(nums):


    n = len(nums)


    dp = [1] * n



    for i in range(n):


        for j in range(i):


            if nums[j] < nums[i]:


                dp[i] = max(

                    dp[i],

                    dp[j]+1

                )



    return max(dp)




nums = [

10,9,2,5,3,7,101,18

]


print(
    LIS(nums)
)





#Unique Paths (Grid DP)
def uniquePaths(m,n):


    dp = [

        [1]*n

        for _ in range(m)

    ]



    for row in range(1,m):


        for col in range(1,n):


            dp[row][col] = (

                dp[row-1][col]

                +

                dp[row][col-1]

            )



    return dp[m-1][n-1]




print(
    uniquePaths(
        3,
        3
    )
)
