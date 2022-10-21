# ЗАДАНИЕ 17.9.1 (HW-03)
def insertion_sort(nums):
    ''' Метод сортировки вставками '''
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert


def binary_search(array, element, left, right):
    ''' Метод двоичного поиска '''
    if array[0] == element:
        return left
    elif right - left < 1:
        if array[left] >= element:
            return left - 1
        return left

    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


text = input('Введите последовательность чисел через пробел: ').split()
while not all([i.isdigit() for i in text]) or text[0] == text[-1]:
    print('Внимание! Некорректный ввод.\nПоследовательность должна состоять '
          'из не менее 2 элементов и содержать только числа!')
    text = input('Пожалуйста, повторите ввод чисел: ').split()
sp = list(map(int, text))
insertion_sort(sp)
ind_end = sp.index(sp[-1])

text = input(f'Введите любое число: ')
while not text.isdigit() or not ((sp[0]+1) <= int(text) <= sp[-1]):
    if not text.isdigit():
        print('Внимание, некорректный ввод!\nЭто не число.')
    elif int(text) < (sp[0] + 1) or int(text) > sp[-1]:
        print('Ваше число выходит за пределы диапазона числовой последовательности.')
    text = input(f'Введите число в интервале от {(sp[0] + 1)} до {sp[-1]}: ')
num = int(text)

res = binary_search(sp, num, 0, ind_end)
otstup = str(sp[:res]).index(']') + 2
print(f'Отсортированный список:\n{sp}')
if res == 0:
    print(f' ^\nиндекс = {res}')
else:
    print(' ' * otstup + '^\n'+ ' ' * (otstup - 2), f'индекс = {res}')
print(f'Элемент, предшествующий числу {num}: [{sp[res]}], стоящий на {res} позиции.')
