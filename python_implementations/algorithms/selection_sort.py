def selection_sort(arr: list) -> list:
    # Last iteration is unnecessary because its sorted by then.
    for i in range(len(arr) - 1):
        min_val = (arr[i], i)
        for j in range(i, len(arr)):
            if arr[j] < min_val[0]:
                min_val = (arr[j], j)
        _ = arr.pop(min_val[1])
        arr.insert(i, min_val[0])
    return arr


def test_selection_sort():
    res = selection_sort([3, 1, 2, 10, 8, 6, 6])
    assert res == [1, 2, 3, 6, 6, 8, 10]
