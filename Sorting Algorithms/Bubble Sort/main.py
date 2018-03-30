"""
冒泡排序

 算法描述
1. 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
3. 针对所有的元素重复以上的步骤，除了最后一个；
重复步骤1~3，直到排序完成。
"""
import sys


class Solution:
    def bubble_sort(self, arr):
        """
        :type arr: List[int]
        """
        for ii in range(len(arr)):
            for jj in range(len(arr) - 1 - ii):
                if arr[jj] > arr[jj + 1]:
                    min_value = arr[jj + 1]
                    arr[jj+1] = arr[jj]
                    arr[jj] = min_value
        return arr

if __name__ == '__main__':
    S = Solution()
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    print(S.bubble_sort(values))