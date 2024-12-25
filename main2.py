# Сортировка слиянием

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделяем массив на две части
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Сортируем левую половину
    right = merge_sort(arr[mid:])  # Сортируем правую половину

    # Сливаем отсортированные части
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Слияние двух отсортированных массивов
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Пример использования
array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(array)
print("Исходный массив:", array)
print("Отсортированный массив:", sorted_array)
