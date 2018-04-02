"""
快速排序

参考：http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
1. 选取第一个数为中心值pivotvalue，索引 leftmark=1, rightmark=len(arr) - 1(序列最后一个数)
2. 左边从中心值后面开始搜索，leftmark++，元素小于中心值继续，大于中心值停止，数记为max_than_pivotvalue，此时
3. 右边从最后一个元素往前搜索,rightmark--，元素大于中心值继续，小于中心值停止,数记为min_than_pivotvalue
4. 交换max_than_pivotvalue， min_than_pivotvalue
5. 接着上面leftmark rightmark继续搜索交换
6. 直至接着上面leftmark > rightmark,交换pivotvalue和rightmark的值
这样pivotvalue左边全是小于其的数 右边全是大于其的数
分为两个子序列继续快排

输入是 54 26 93 17 77 31 44 55 20
"""
import sys


class Solution:
    def quickSort(self, alist, first, last):
        if first < last:
            splitpoint = self.partition(alist, first, last)
            self.quickSort(alist, first, splitpoint - 1)
            self.quickSort(alist, splitpoint + 1, last)

    def partition(self, alist, first, last):
        pivotvalue = alist[first]  # 第一个元素作为中心值

        leftmark = first + 1    # 左边从中心值后面开始搜索
        rightmark = last        # 右边从最后一个元素往前搜索

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark

if __name__ == '__main__':
    S = Solution()
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split(' ')))
    S.quickSort(values, 0, len(values)-1)
    print(values)
