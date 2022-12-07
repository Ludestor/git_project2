def sort(nums):
    length = len(nums)
    swapped = True
    start_index = 0
    end_index = length - 1
    while (swapped == True):
        swapped = False
        for i in range(start_index, end_index):
            if (nums[i] > nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        if (not (swapped)):
            break
        swapped = False
        end_index = end_index - 1
        for i in range(end_index - 1, start_index - 1, -1):
            if (nums[i] > nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        start_index = start_index + 1

print('Шейкерная сортировка:')
nums = [11, 9, 14, 88, 0, 16, 2, 28]
sort(nums)
print(nums)