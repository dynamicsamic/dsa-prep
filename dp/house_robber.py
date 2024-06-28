def house_robber_dp(nums: list[int]) -> int:
    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0]

    for i in range(1, len(nums)):
        dp[i + 1] = max(dp[i], (dp[i - 1] + nums[i]))

    return dp[-1]


def house_robber_vars(nums: list[int]) -> int:
    a = 0
    b = nums[0]

    for i in range(1, len(nums)):
        a, b = b, max(b, (a + nums[i]))

    return b

print(house_robber_vars([2, 7, 9, 3, 1]))
print(house_robber_vars([1, 2, 3, 1]))
print(house_robber_vars([2]))
print(house_robber_vars([4, 1, 2]))
print(house_robber_vars([1, 4, 5, 3, 3]))