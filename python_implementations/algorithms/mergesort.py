def merge_sorted_arrays(arr1: list, arr2: list) -> list:
    it1 = ListIterator(arr1)
    it2 = ListIterator(arr2)
    result = []
    # Check if either array is empty
    if not it1.arr:
        return it2.arr
    if not it2.arr:
        return it1.arr
    # Iterate through items
    while not (it1.done and it2.done):
        if it1.done:
            result.extend(it2.arr[it2.current_ind :])
            return result
        elif it2.done:
            result.extend(it1.arr[it1.current_ind :])
            return result
        else:
            if it1.get() <= it2.get():
                result.append(it1.get())
                it1.next()
            else:
                result.append(it2.get())
                it2.next()
    return result


class ListIterator:
    def __init__(self, input_list: list):
        self.arr: list = input_list
        self.done: bool = False
        self.current_ind: int = 0

    def next(self):
        self.current_ind += 1
        if self.current_ind > len(self.arr) - 1:
            self.done = True

    def get(self):
        return self.arr[self.current_ind]


def mergesort(arr: list) -> list:
    if len(arr) == 1:
        return arr
    else:
        middle_ind = len(arr) // 2
        left = arr[:middle_ind]
        right = arr[middle_ind:]
        return merge_sorted_arrays(mergesort(left), mergesort(right))


def test_merge_sort():
    res = mergesort([3, 1, 2, 10, 8, 6, 6])
    assert res == [1, 2, 3, 6, 6, 8, 10]
    res = mergesort([3, 1, 2, 10, 8, 6])
    assert res == [1, 2, 3, 6, 8, 10]
