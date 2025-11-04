import random, time, math
from copy import deepcopy

def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def merge_sort(a):
    if len(a) <= 1:
        return a[:]
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    res = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i+=1
        else:
            res.append(right[j]); j+=1
    res.extend(left[i:]); res.extend(right[j:])
    return res

def quick_sort(a):
    if len(a) <= 1:
        return a[:]
    pivot = a[len(a)//2]
    left = [x for x in a if x < pivot]
    mid = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def heapify(a, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heap_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n//2-1, -1, -1):
        heapify(a, n, i)
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)
    return a

ALGORITHMS = {
    'selection': selection_sort,
    'bubble': bubble_sort,
    'merge': merge_sort,
    'quick': quick_sort,
    'heap': heap_sort,
}

def time_it(fn, data):
    start = time.perf_counter()
    out = fn(data)
    end = time.perf_counter()
    return end-start, out

def validate_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def run_all():
    sizes = [100, 500, 1000]
    trials = 3
    results = []
    for n in sizes:
        print(f"\nDataset size: {n}")
        data = [random.randint(0, n*10) for _ in range(n)]
        for name, fn in ALGORITHMS.items():
            total = 0.0
            ok = True
            for t in range(trials):
                d = data[:]  # same dataset per algorithm per size
                ttime, out = time_it(fn, d)
                total += ttime
                if not validate_sorted(out):
                    ok = False
            avg = total / trials
            print(f"{name:10} | avg {avg:.6f}s | valid: {ok}")
            results.append((n, name, avg, ok))
    # write simple report
    import datetime
    fn = f"results-report-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"
    with open(fn, 'w') as f:
        for r in results:
            f.write(f"size={r[0]}\talg={r[1]}\tavg={r[2]:.6f}\tvalid={r[3]}\n")
    print(f"\nReport written to {fn}")

if __name__ == '__main__':
    run_all()
