def selection_sort(arr: list) -> list:
    # Last iteration is unnecessary because its sorted by then.
    for i in range(len(arr) - 1):
        min_val = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_val]:
                min_val = j
        (arr[i], arr[min_val]) = (arr[min_val], arr[i])
    return arr


def test_selection_sort():
    res = selection_sort([3, 1, 2, 10, 8, 6, 6])
    assert res == [1, 2, 3, 6, 6, 8, 10]
