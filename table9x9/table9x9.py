# -*- coding: utf-8 -*-
# __author__ = 'lidongliang soul136186847@outlook.com'


class PrintTable(object):
    """打印99乘法表"""

    def __init__(self):
        print('开始打印9x9乘法表')
        self.print99()

    def print99(self):
        for i in range(1, 10):
            for j in range(1, i + 1):
                print('%dX%d=%2s ' % (j, i, j * i), end="")
            print(end="\n")


if __name__ == '__main__':
    pt = PrintTable()
