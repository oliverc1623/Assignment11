"""
random file with sorting algorithms
"""


def merge(left_list, right_list):
    print("WE are in MERGe")
    index_a = 0
    index_b = 0
    c = []

    while index_a < len(left_list) and index_b < len(right_list):
        if left_list[index_a] <= right_list[index_b]:
            c.append(left_list[index_a])
            index_a += 1
        else:
            c.append(right_list[index_b])
            index_b += 1

    c.extend(left_list[index_a:])
    c.extend(right_list[index_b:])
    print("RECENTLY MERGED: " + str(c))
    return c


def merge_sort(alist):
    """

    :param alist:
    :return:
    """
    if len(alist) == 0 or len(alist) == 1:
        print("base case!")
        return alist[:len(alist)]
    mid = len(alist)//2
    left_list = alist[0:mid]
    right_list = alist[mid:len(alist)]
    print("right list: " + str(left_list))
    newlist1 = merge_sort(left_list)
    print("left list: " + str(right_list))
    newlist2 = merge_sort(right_list)
    newlist = merge(newlist1, newlist2)
    return newlist


def main():
    sample_list = [44, 23, 1, -100, 27, 80, 99, 17, 4, 7, 13]
    print("FINAL: " + str(merge_sort(sample_list)))


if __name__ == '__main__':
    main()