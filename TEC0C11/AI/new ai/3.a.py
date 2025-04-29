def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
arr=[5, 2, 9, 1, 5, 6]
selection_sort(arr)
print("Sorted array:", arr)


### if __name__ == '__main__':
   # arr = list(int, input("Enter numbers separated by spaces: ").split())
    #sorted_arr = selection_sort(arr)
    #print("Sorted array:", sorted_arr)
    