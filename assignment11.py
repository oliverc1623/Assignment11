"""
Oliver Chang
CSCI51p
11/30/2018
Assignment 11
This program will compare the runtime of two different algorithms

Sources found online:
I google searched "recusrive binary search" and clicked on the first link only
https://www.geeksforgeeks.org/binary-search/
"""

import time


def linear_search(alist, value):
    """
    This list returns the index where alist contains value. If there is no matching value, it will return -1
    :param alist: list - list of ints
    :param value: int - desired int we're locating
    :return: int - position of value or -1 if value is not in alist
    """
    for i in range(len(alist)):
        if alist[i] == value:
            return i
    return -1


def binary_search_helper(alist, value, start, end):
    """

    :param alist:
    :param value:
    :param start:
    :param end:
    :return:
    """
    mid = int((end + start) / 2)
    if end <= start:
        return -1
    if alist[mid] == value:
        return mid
    elif alist[mid] < value:
        return binary_search_helper(alist, value, mid + 1, end)
    elif alist[mid] > value:
        return binary_search_helper(alist, value, start, mid - 1)


def binary_sort(alist, value):
    """
    Binary sort
    :param alist:
    :param value:
    :return:
    """
    return binary_search_helper(alist, value, 0, len(alist))


def sorted_comparison():
    target = -1
    current_list = [1, 2]
    while len(current_list) < 1048576:
        start = time.time()
        linear_search(current_list, target)
        end = time.time()
        elapsed_time = end - start
        print(len(current_list), elapsed_time)



def main():
    sorted_comparison()


if __name__ == '__main__':
    main()