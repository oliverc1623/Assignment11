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
from random import randint


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


def binary_search(alist, value):
    """
    Binary sort
    :param alist:
    :param value:
    :return:
    """
    return binary_search_helper(alist, value, 0, len(alist))


def get_doubled_sorted_list(alist):
    doubled = []
    for i in range(len(alist) * 2):
        doubled.append(i)
    return doubled


def get_doubled_unsorted_list(alist):
    doubled = []
    for i in range(len(alist) * 2):
        doubled.append(randint(1, 1000))
    return doubled


def sorted_comparison():
    target = -1
    current_list = [1, 2]
    while len(current_list) < 2097152:

        start_linear = time.time()
        linear_search(current_list, target)
        end_linear = time.time()
        elapsed_time_linear = end_linear - start_linear

        start_binary = time.time()
        binary_search(current_list, target)
        end_binary = time.time()
        elapsed_time_binary = end_binary - start_binary

        print(str(len(current_list)) + " " + str(elapsed_time_linear) + " " + str(elapsed_time_binary))
        current_list = get_doubled_sorted_list(current_list)


def unsorted_comparison():
    target = -1
    current_list = [2, 1]
    while len(current_list) < 2097152:
        start_linear = time.time()
        linear_search(current_list, target)
        end_linear = time.time()
        elapsed_time_linear = end_linear - start_linear

        start_binary = time.time()
        binary_search(current_list, target)
        end_binary = time.time()
        elapsed_time_binary = end_binary - start_binary

        print(str(len(current_list)) + " " + str(elapsed_time_linear) + " " + str(elapsed_time_binary))
        current_list = get_doubled_unsorted_list(current_list)


def main():
    print("Sorted comparison: ")
    sorted_comparison()
    print("Unsorted comparison: ")
    unsorted_comparison()


if __name__ == '__main__':
    main()