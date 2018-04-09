"""
二分法

二分法是用来在一个有序数组中到目标数的位置
"""
import sys


class Solution:
    def binary_search(self, arr, target):
        start = 0
        end = len(arr) - 1

        while start + 1 < end:
            mid = int(start + (end - start)/2)
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                start = mid
            else:
                end = mid
        if arr[start] == target:
            return start
        elif arr[end] == target:
            return end
        else:
            raise Exception("No Target!")

if __name__ == '__main__':
    S = Solution()
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split(' ')))
    target = int(input())
    ind = S.binary_search(values, target)
    print(ind)