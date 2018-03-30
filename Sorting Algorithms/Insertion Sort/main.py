"""
插入排序

 算法描述
数据从后往前依次扫描，如果比前面元素小，则把这个元素放在前面元素之前

1. 从第一个元素开始，该元素可以认为已经被排序；
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描；
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置；
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
5. 将新元素插入到该位置后；
重复步骤2~5。
"""
import sys


class Solution:
    def select_sort(self, arr):
        """
        :type arr: List[int]
        """
        for ii in range(0, len(arr)-1):
            sel_index = ii
            cur_values = arr[ii + 1]  # 要插入的元素
            while arr[sel_index] > cur_values and sel_index >= 0:  # 判断是否前面的数较大
                arr[sel_index + 1] = arr[sel_index]                 # 将较大的数后移一位
                sel_index -= 1
            arr[sel_index + 1] = cur_values
        return arr

if __name__ == '__main__':
    S = Solution()
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    print(S.select_sort(values))