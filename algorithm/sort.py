# 选择排序算法

class Sort:
    """
    def __init__(self,arr):
        self.arr = arr
    """
    @staticmethod
    def selection_sort(arr):
        """
        选择排序
        :param arr:
        :return:
        """
        for i in range(len(arr) - 1):
            # 记录最小数的索引
            minIndex = i
            for j in range(i+1 , len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            # i 不是最小数时，将 i 和最小数进行交换
            if i != minIndex:
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr

    @staticmethod
    def bubble_sort1(arr):
        """
        冒泡
        :param arr: 无序
        :return: arr有序
        """
        for i in range(len(arr)):
            for j in range(i, len(arr)-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def bubble_sort2(arr):
        """
        冒泡
        :param arr: 无序
        :return: arr有序
        """
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr


if __name__ == "__main__":
    list_a = [12, 34, 2, 42, 31, 25]
    list_b = [12, 34, 2, 42, 31, 25, 19]
    list_c = [12, 34, 2, 42, 31, 25, 20]
    print(Sort.selection_sort(list_a))
    print(Sort.bubble_sort1(list_c))
    print(Sort.bubble_sort2(list_b))

