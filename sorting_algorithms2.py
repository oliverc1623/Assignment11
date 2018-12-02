# How would I order a deck of cards in real life?
# - I would take

# Sorting algorithms:
# 1. Selection Sort
#    For each position in the deck: find the card that should be there and put it there
# 2. Insertion Sort
#    For each position in deck: put that card in right place


# Selection sorting algorithm
def selection_sort(list):
    for pos in range(len(list)):
        min_pos = pos
        for i in range(pos+1, len(list)):
            if list[i] < list[pos]:
                min_pos = i
        # put it in position pos
        tmp = list[pos]
        list[pos] = list[min_pos]
        list[min_pos] = tmp


# Insertion sorting algorithm
def insertion_sort(list):
    for pos in range(len(list)):
        current_pos = pos
        while current_pos > 0 and list[current_pos-1] > list[current_pos]:
            tmp = list[current_pos]
            list[current_pos] = list[current_pos-1]
            list[current_pos-1] = tmp
            current_pos = current_pos-1
            current_pos -= 1

# What makes a good algorithm:
# 1. Correctness
# 2. Fastness
# 3. Less space

# Constant time operation: its time doesn't depend on the size of length of anything. Always roughly the same.
# Time is bounded above by some number.

# Example Basic steps:
# - Input/output of a number
# - Access value of a variable, list element, or object attr
# - Assign to a variable, list element, or object attr
# - Do one arithmetic or logical operation
# - Call a function
# Concatenation is not a basic step

# Counting Steps

# Big O notation
# n^2 + 2n + 5 O(n^2)
# 1000n + 25000 O(n)
# 2^n/15 + n^100 O(2^n)
# nlog(n) + 25n O(nlog(n))

# Merge sort
# Recursively sorting using Mergesort


def merge(lst, start, middle, end):
    olst = lst[start:middle].copy()
    pos = start
    i = 0
    j = middle
    while i < len(lst):
        if j < end and olst[i] < lst[j]:
            lst[pos] = olst[i]
            pos += 1
            j += 1
        else:
            lst[pos] = olst[i]
            i += 1
        pos += 1


def merge_sort(lst, start, end):
    if end - start < 2:
        return
    middle = int((end+start)/2)
    merge_sort(lst, start, middle)
    merge_sort(lst, middle, end)
    merge(lst, start, middle, end)


def main():
    lst = [10, 46, -10, -100, 0, 47, 4, 23]
    merge_sort(lst, 0, len(lst))


if __name__ == '__main__':
    main()