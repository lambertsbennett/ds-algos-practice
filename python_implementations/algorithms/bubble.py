def bubble_sort(arr: list) -> list:
    n = len(arr) - 1
    while n > 0:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
        n -= 1
    return arr


def test_bubble_sort():
    res = bubble_sort([3, 1, 2, 10, 8, 6, 6])
    assert res == [1, 2, 3, 6, 6, 8, 10]
