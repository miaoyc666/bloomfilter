#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : test.py
Author       : miaoyc
Create date  : 2021/10/8 14:47
Description  : 测试程序
"""

import bf


if __name__ == '__main__':
    # init data
    bf_filter = bf.BloomFilter()
    for i in range(100000):
        bf_filter.add("test_url_{0}".format(i))   

    # query 
    print("miaoyc: ", bf_filter.contains("miaoyc"))
    print("test_url_-1: ", bf_filter.contains("test_url_-1"))
    print("test_url_99999: ", bf_filter.contains("test_url_99999"))
