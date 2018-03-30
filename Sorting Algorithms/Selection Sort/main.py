"""
选择排序

 算法描述
从第一个元素查找，如果后面找到比这个元素小的则交换位置，然后继续往后找，如果有小的继续交换
"""
import sys


class Solution:
    def select_sort(self, arr):
        """
        :type arr: List[int]
        """
        for ii in range(len(arr)):
            min_index = ii
            for jj in range(ii+1, len(arr)):
                if arr[jj] < arr[min_index]:
                    min_index = jj
            temp = arr[ii]
            arr[ii] = arr[min_index]
            arr[min_index] = temp
        return arr

if __name__ == '__main__':
    S = Solution()
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    print(S.select_sort(values))