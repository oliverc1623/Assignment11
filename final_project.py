"""
Final programming assignment
CSCI51p
Oliver Chang
final_project
11/29/2018
This program will analyze data from AirB&B
"""

from scipy.stats.stats import spearmanr


def price_satisfaction(filename):
    """

    :param file_name:
    :return:
    """
    new_list = []

    file_in = open(filename, "r")
    file_in.readline()
    for i in file_in.readlines():
        sublist = []
        split_string = i.split(",")
        price = float(split_string[13])
        satisfaction = float(split_string[9])

        sublist.append(price)
        sublist.append(satisfaction)
        new_list.append(sublist)

    return new_list


def correlation(l):
    """

    :param l:
    :return:
    """
    price = []
    rating = []
    for i in l:
        # print(i)
        price.append(i[0])
        rating.append(i[1])
    result = spearmanr(price, rating)
    correlation = result.correlation
    pvalue = result.pvalue

    t = (correlation, pvalue)

    return t


def host_listings(filename):
    hostings = {}
    file_in = open(filename, "r")
    file_in.readline()

    hosts = []
    room_ids_list = []
    host_ids_list = []
    for i in file_in.readlines():
        split_string = i.split(",")
        host_ids_list.append(int(split_string[2]))
    print(host_ids_list)


def main():
    """

    :return:
    """
    file_name = "tomslee_airbnb_brno_1500_2017-07-20.csv"
    #print(correlation(price_satisfaction(file_name)))
    host_listings(file_name)


if __name__ == '__main__':
    main()
