def sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

print('Пузырьковая сортировкa:')
nums = [11, 9, 14, 88, 0, 16, 2, 28]
sort(nums)
print(nums)