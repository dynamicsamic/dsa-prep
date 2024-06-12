def two_sum(nums: list[int], target: int) -> list[int]:
    complements = {}

    for i in range(len(nums)):
        if nums[i] in complements:
            return [complements[nums[i]], i]
        complements[target - nums[i]] = i


tests = [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)]

for nums, target in tests:
    print(two_sum(nums, target))
