"""
希尔排序

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
    def shellSort(self, alist):
        sublistcount = len(alist) // 2
        while sublistcount > 0:

            for startposition in range(sublistcount):
                self.gapInsertionSort(alist, startposition, sublistcount)

            print("After increments of size", sublistcount,
                  "The list is", alist)

            sublistcount //= 2

    def gapInsertionSort(self, alist, start, gap):
        for i in range(start + gap, len(alist), gap):

            currentvalue = alist[i]
            position = i

            while position >= gap and alist[position - gap] > currentvalue:
                alist[position] = alist[position - gap]
                position = position - gap

            alist[position] = currentvalue


if __name__ == '__main__':
    S = Solution()
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    S.shellSort(values)
    print(values)