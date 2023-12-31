from typing import List

def merge_sorted_arrays(arr1: List, arr2: List) -> List:
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
            result.extend(it2.arr[it2.current_ind:])
            return result
        elif it2.done:
            result.extend(it1.arr[it1.current_ind:])
            return result
        else:
            if it1.get() <= it2.get():
                result.append(it1.get())
                it1.next()
            else:
                result.append(it2.get())
                it2.next()
    return result
    


class ListIterator():
    def __init__(self, input_list: List):
        self.arr: List = input_list
        self.done: bool = False
        self.current_ind: int = 0
    
    def next(self):
        self.current_ind += 1
        if self.current_ind > len(self.arr) - 1:
            self.done = True
    
    def get(self):
        return self.arr[self.current_ind]



assert merge_sorted_arrays([0,1,2], [3,4,5]) == [0,1,2,3,4,5]
assert merge_sorted_arrays([0,3,5], [1,2,6]) == [0,1,2,3,5,6]
assert merge_sorted_arrays([-1, 4, 5], [1, 2, 3, 4]) == [-1, 1, 2, 3, 4, 4, 5]
assert merge_sorted_arrays([1,2,3,4,5], [-2, -1, 10]) == [-2,-1,1,2,3,4,5,10]
assert merge_sorted_arrays(['a', 'b', 'c'], ['d', 'e', 'f']) == ['a', 'b', 'c', 'd', 'e', 'f']
assert merge_sorted_arrays([], [1,2,3]) == [1,2,3]
assert merge_sorted_arrays([1,2,3], []) == [1,2,3]