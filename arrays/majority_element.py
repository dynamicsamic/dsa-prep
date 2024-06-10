def majority_element(nums: list[int]) -> int:
    nums.sort()

    length = len(nums)
    i = 0
    counter = 0

    while i < length:
        majority_el = nums[i]
        while nums[i] == majority_el:
            counter += 1
            i += 1
            if i == length:
                break
        if counter > length // 2:
            return majority_el

        counter = 0


def majority_element_bonus(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]


nums = [1, 1, 1, 2, 2, 2, 2]

nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums2))
[1, 1, 3, 3, 2, 2, 2]
