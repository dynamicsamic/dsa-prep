def remove_element(nums: list[int], val: int) -> int:
    valid = [num for num in nums if num != val]

    for i in range(len(valid)):
        nums[i] = valid[i]

    return len(valid)


nums = [3, 2, 2, 3]
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
print(remove_element(nums, 3))
print(remove_element(nums2, 2))
