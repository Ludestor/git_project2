def sort(nums):
    step = int(len(nums) / 1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(nums):
            if nums[i] > nums[i + step]:
                nums[i], nums[i + step] = nums[i + step], nums[i]
                swap += 1
            i = i + 1
        if step > 1:
            step = int(step / 1.247)

nums = [11, 9, 14, 88, 0, 16, 2, 28]
sort(nums)
print('Результат сортировки:')
print(nums)