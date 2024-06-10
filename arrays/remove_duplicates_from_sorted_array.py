def remove_duplicates(nums: list[int]) -> None:
    i = 0
    current = nums[i]
    seen = {current}

    while i < len(nums):
        current = nums[i]
        if current in seen:
            swap_place = i
            while nums[i] == current:
                i += 1
            if i == len(nums):
                break
            nums[swap_place] = nums[i]
            seen.add(nums[i])
        else:
            seen.add(current)
            i += 1


nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums2 = [1, 1, 2]


def remove_duplicates2(nums: list[int]) -> None:
    current = nums[0]
    seen = [current]

    for i in range(1, len(nums)):
        if nums[i] != current:
            current = nums[i]
            seen.append(current)

    for i in range(len(seen)):
        nums[i] = seen[i]

    return len(seen)


print(remove_duplicates2(nums2))
