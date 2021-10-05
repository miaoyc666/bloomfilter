#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : bf.py
Author       : miaoyc
Create date  : 2021/10/5 23:47
Description  : 布隆过滤器实现
"""

import mmh3
from bitarray import bitarray


# Implement a simple bloom filter with murmurhash algorithm.
# Bloom filter is used to check wether an element exists in a collection.
# It has a good performance in big data situation.
# It may has positive rate depend on hash functions and elements count.


BIT_SIZE = 5000000


class BloomFilter:

    def __init__(self):
        # Initialize bloom filter, set size and all bits to 0
        self.bits = bitarray(BIT_SIZE)
        self.bits.setall(0)

    def get_position(self, url):
        # Here use 5 hash functions.
        # Get points positions in bit vector.
        point0 = mmh3.hash(url, 50) % BIT_SIZE
        point1 = mmh3.hash(url, 51) % BIT_SIZE
        point2 = mmh3.hash(url, 52) % BIT_SIZE
        point3 = mmh3.hash(url, 53) % BIT_SIZE
        point4 = mmh3.hash(url, 54) % BIT_SIZE
        return [point0, point1, point2, point3, point4]

    def contains(self, url):
        # Check if a url is in a collection
        point_list = self.get_postion(url)
        return all(point_list)

    def add(self, url):
        # Add a url, and set points in bitarray to 1 (Points count is equal to hash funcs count.)
        point_list = self.get_position(url)

        for b in point_list:
            self.bit_array[b] = 1
