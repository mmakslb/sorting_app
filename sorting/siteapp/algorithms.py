from datetime import datetime


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        execution_time = datetime.now() - start_time
        return result, execution_time
    return wrapper


class AbstractSort:

    def sort(self, array):
        pass


class BubbleSort(AbstractSort):

    @time_decorator
    def sort(self, array):
        n = len(array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array


class InsertionSort(AbstractSort):

    @time_decorator
    def sort(self, array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array


class MergeSort(AbstractSort):

    @time_decorator
    def sort(self, array):
        def merge_sort_in(array):
            if len(array) > 1:
                mid = len(array) // 2
                left_half = array[:mid]
                right_half = array[mid:]

                merge_sort_in(left_half)
                merge_sort_in(right_half)

                i = 0
                j = 0
                k = 0
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        array[k] = left_half[i]
                        i = i + 1
                    else:
                        array[k] = right_half[j]
                        j = j + 1
                    k = k + 1

                while i < len(left_half):
                    array[k] = left_half[i]
                    i = i + 1
                    k = k + 1

                while j < len(right_half):
                    array[k] = right_half[j]
                    j = j + 1
                    k = k + 1
            return array
        merge_sort_in(array)
        return array
