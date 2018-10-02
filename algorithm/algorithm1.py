#!/usr/bin/env/python
# -*-coding:utf-8 -*-
# 设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
# 如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
# 如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。


def judge(l):
    for i in l:
        try:
            if i.isdigit() == False:
                raise NameError;
        except NameError:
            return 0;
    else:

        l.sort(reverse=True)
        n = int(''.join(l))
        return n;


if __name__ == '__main__':

    while True:
        n = input()
        l = [];
        str = input()
        l = str.split(' ');

        print(judge(l))
