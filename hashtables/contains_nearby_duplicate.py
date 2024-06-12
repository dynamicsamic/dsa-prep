def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    seen = {}

    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False


tests = [
    ([1, 2, 2, 1], 3, True),
    ([1, 2, 3, 1], 1, False),
    ([1, 2, 3, 1, 1], 1, True),
    ([1, 0, 1, 1], 1, True),
    ([1, 2, 3, 1, 2, 3], 2, False),
    ([1, 2, 3, 1], 3, True),
]

for nums, k, res in tests:
    assert contains_nearby_duplicate(nums, k) is res
print("All tests passed")
