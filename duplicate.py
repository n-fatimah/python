def contains_duplicate(nums):
    chk = set()
    for num in nums:
        if num in chk:
            return True
        chk.add(num)

    return False

nums1 = [1, 2, 3, 1]
print(contains_duplicate(nums1))