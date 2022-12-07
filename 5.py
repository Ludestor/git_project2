def sort(nums, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        p = part(nums, start, end)
        sort(nums, start, p)
        sort(nums, p + 1, end)


def part(nums, start, end):
    pivot = nums[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and nums[i] <= pivot):
            i = i + 1
        while (i <= j and nums[j] >= pivot):
            j = j - 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            nums[start], nums[j] = nums[j], nums[start]
            return j


nums = [11, 9, 14, 88, 0, 16, 2, 28]
nums = [int(x) for x in nums]
sort(nums, 0, len(nums))
print('Результат сортировки:')
print(nums)