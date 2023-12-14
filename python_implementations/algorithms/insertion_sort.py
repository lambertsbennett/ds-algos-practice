def insertion_sort(arr: list) -> list:
    i = 1
    while i < len(arr):
        if arr[i] < arr[0]:
            val = arr.pop(i)
            arr.insert(0, val)
        elif arr[i] > arr[i - 1]:
            i += 1
            continue
        else:
            for j in range(0, i - 1):
                tmp_lb = arr[j]
                tmp_ub = arr[j + 1]
                if (arr[i] >= tmp_lb) and (arr[i] <= tmp_ub):
                    val = arr.pop(i)
                    arr.insert(j + 1, val)
                    i += 1
                    break
    return arr


def test_insertion_reversed_sort():
    res = insertion_sort([10, 9, 8])
    assert res == [8, 9, 10]


def test_insertion_sort_asc():
    res = insertion_sort([1, 2, 3, 10])
    assert res == [1, 2, 3, 10]


def test_insertion_sort_rand():
    res = insertion_sort([3, 1, 2, 10, 8, 6, 6])
    assert res == [1, 2, 3, 6, 6, 8, 10]
