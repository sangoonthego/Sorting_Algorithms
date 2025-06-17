import time

def bubble_sort(arr, reverse=False):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]) ^ reverse:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr, reverse=False):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        ext = i
        for j in range(i + 1, n):
            if (arr[j] < arr[ext]) ^ reverse:
                ext = j
        arr[i], arr[ext] = arr[ext], arr[i]
    return arr

def insertion_sort(arr, reverse=False):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and (arr[j] > key) ^ reverse:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr, reverse=False):
    def merge(L, R):
        result = []
        i = j = 0
        while i < len(L) and j < len(R):
            if (L[i] <= R[j]) ^ reverse:
                result.append(L[i])
                i += 1
            else:
                result.append(R[j])
                j += 1
        result.extend(L[i:])
        result.extend(R[j:])
        return result

    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], reverse)
    right = merge_sort(arr[mid:], reverse)
    return merge(left, right)

def quick_sort(arr, reverse=False):
    arr = arr.copy()
    def quick_sort_rec(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_rec(low, pi - 1)
            quick_sort_rec(pi + 1, high)

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if (arr[j] <= pivot) ^ reverse:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    quick_sort_rec(0, len(arr) - 1)
    return arr

def heap_sort(arr, reverse=False):
    arr = arr.copy()
    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and (arr[l] > arr[largest]) ^ reverse:
            largest = l
        if r < n and (arr[r] > arr[largest]) ^ reverse:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
    return arr

def counting_sort(arr, reverse=False):
    arr = arr.copy()
    if not arr: return []
    max_val, min_val = max(arr), min(arr)
    range_val = max_val - min_val + 1
    count = [0] * range_val
    for num in arr:
        count[num - min_val] += 1
    if reverse:
        for i in range(len(count) - 2, -1, -1): count[i] += count[i + 1]
    else:
        for i in range(1, len(count)): count[i] += count[i - 1]
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    return output

def counting_sort_exp(arr, exp, reverse=False):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    if reverse:
        for i in range(8, -1, -1): count[i] += count[i + 1]
    else:
        for i in range(1, 10): count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    return output

def radix_sort(arr, reverse=False):
    arr = arr.copy()
    if not arr: return []
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        arr = counting_sort_exp(arr, exp, reverse)
        exp *= 10
    return arr

def shell_sort(arr, reverse=False):
    arr = arr.copy()
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and (arr[j - gap] > temp) ^ reverse:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def test_algorithms(arr, reverse=False):
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,
        "Counting Sort": counting_sort,
        "Radix Sort": radix_sort,
        "Shell Sort": shell_sort,
    }
    results = []
    for name, func in algorithms.items():
        start = time.time()
        sorted_arr = func(arr, reverse=reverse)
        end = time.time()
        results.append((name, round(end - start, 6), sorted_arr))
    return results

if __name__ == "__main__":
    input_string = input("Input the list of numbers: ")
    arr = list(map(int, input_string.strip().split()))
    order = input("Sort descending? (y/n): ").strip().lower()
    reverse = order == 'y'
    
    results = test_algorithms(arr, reverse)
    for name, t, sorted_arr in results:
        print(f"{name:15} | Time: {t:.6f}s | Result: {sorted_arr}")
