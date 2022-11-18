n = int(input("Количество элементов массива: "))
nums = []
for i in range(1, n+1):
    x = int(input(f'Введите {i} элемент массива: '))
    nums.append(x)
m = sorted(nums)[n // 2]
print(sum(abs(v - m) for v in nums))