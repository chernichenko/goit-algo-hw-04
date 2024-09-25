import random
import timeit

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def test_sorting_algorithms():
    sizes = [100, 1000, 5000, 10000]
    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]
        
        # Тестування Merge Sort
        merge_data = data.copy()
        merge_time = timeit.timeit(lambda: merge_sort(merge_data), number=100)
        print(f"Merge Sort for size {size}: {merge_time:.5f} seconds")
        
        # Тестування Insertion Sort
        insertion_data = data.copy()
        insertion_time = timeit.timeit(lambda: insertion_sort(insertion_data), number=100)
        print(f"Insertion Sort for size {size}: {insertion_time:.5f} seconds")
        
        # Тестування Timsort
        timsort_data = data.copy()
        timsort_time = timeit.timeit(lambda: sorted(timsort_data), number=100)
        print(f"Timsort for size {size}: {timsort_time:.5f} seconds")

def merge_k_lists(lists):
    merged_list = []
    for lst in lists:
        merged_list.extend(lst)
    merge_sort(merged_list)
    return merged_list

if __name__ == "__main__":
    test_sorting_algorithms()
    
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)