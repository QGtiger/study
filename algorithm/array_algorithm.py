"""
author:lightfish
time:2018.10.2
notes:在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
"""

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row=len(array)-1
        col=0
        while row>=0 and col<len(array[0]):
            if target == array[row][col]:
                return True
            if target < array[row][col]:
                row-=1
                continue
            if target > array[row][col]:
                col+=1
                continue
        return False