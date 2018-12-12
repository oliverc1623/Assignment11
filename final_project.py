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
    header = file_in.readline()
    comma_count = 0
    for c in header:
        if c == ",":
            comma_count += 1
    # print(comma_count)

    for line in file_in:
        line_comma_count = 0
        for c in line:
            if c == ",":
                line_comma_count += 1

        if line_comma_count == comma_count:
            # print(line)
            sublist = []
            line_splited = line.split(",")
            # print(line_splited)
            price = float(line_splited[13])
            satisfaction = float(line_splited[9])
            if int(line_splited[8]) > 0:
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
    """

    :param filename:
    :return:
    """
    hostings = {}
    file_in = open(filename, "r")
    file_in.readline()
    for i in file_in.readlines():
        split_string = i.split(",")
        if hostings.get(int(split_string[2])) is None:
            hostings[int(split_string[2])] = [int(split_string[0])]
        else:
            room_ids = hostings.get(int(split_string[2]))
            room_ids.append(int(split_string[0]))
            hostings[int(split_string[2])] = room_ids
    return hostings


def num_listings(dict):
    """

    :param dict:
    :return:
    """
    l = []
    num_hosts = []
    max_hostings = 0
    for i in dict.values():
        if max_hostings < len(i):
            max_hostings = len(i)
        num_hosts.append(len(i))
    for i in range(max_hostings + 1): l.append(0)
    for i in range(len(l)):
        for k in num_hosts:
            if i == k:
                l[i] += 1
    return l


def room_prices(filename_list, roomtype):
    """

    :param filename_list:
    :param roomtype:
    :return:
    """
    delta_price = {}
    sorted_files = filename_list[:]
    sorted_files.sort()
    for filename in sorted_files:
        file_in = open(filename, "r")
        file_in.readline()
        for line in file_in.readlines():
            split_header = line.split(",")
            if split_header[3] == roomtype:
                key = int(split_header[0])
                if delta_price.get(key) is None:
                    delta_price[key] = [float(split_header[13])]
                else:
                    prices = delta_price.get(key)
                    prices.append(float(split_header[13]))
                    delta_price[key] = prices
    return delta_price


def price_change(dict):
    """

    :param dict:
    :return:
    """
    prices = []

    for i in dict.values():
        prices.append(i)

    max_percentage_change = ((prices[0][len(prices[0])-1] - prices[0][0])/prices[0][0]) * 100
    starting_price = prices[0][0]
    ending_price = prices[0][len(prices[0])-1]
    t = (max_percentage_change, starting_price, ending_price)
    for i in range(len(prices)):
        if max_percentage_change < (((prices[i][len(prices[i])-1] - prices[i][0])/prices[i][0]) * 100):
            max_percentage_change = (((prices[i][len(prices[i])-1] - prices[i][0])/prices[i][0]) * 100)
            starting_price = prices[i][0]
            ending_price = prices[i][len(prices[i])-1]
            t = (max_percentage_change, starting_price, ending_price)
    return t


def main():
    """

    :return:
    """
    file_name = "tomslee_airbnb_new_york_1438_2017-07-12.csv"
    print(price_satisfaction(file_name))
    print(correlation(price_satisfaction(file_name)))
    # print(host_listings(file_name))
    # print(num_listings(host_listings(file_name)))
    file_list = ["tomslee_airbnb_brno_1258_2017-05-14.csv",
                 "tomslee_airbnb_brno_1500_2017-07-20.csv",
                 "tomslee_airbnb_brno_1383_2017-06-24.csv"]
    output = room_prices(file_list, "Shared room")
    print(price_change(output))


if __name__ == '__main__':
    main()
