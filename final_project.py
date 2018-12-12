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
    This functions returns a list consisting of lists contained with price and overall_satisfaction
    :param filename: string - name of the csv file
    :return: list - list of lists [price, overall_satisfaction]
    """

    # Initialize new list we will return
    new_list = []

    # Open file
    file_in = open(filename, "r")

    # read the header line and find the index of price, overall_satisfaction, and reviews
    header = file_in.readline()
    header_list = header.split(",")
    price_index = header_list.index("price")
    satisfaction_index = header_list.index("overall_satisfaction")
    review_index = header_list.index("reviews")

    # find number of commas in header
    comma_count = 0
    for c in header:
        if c == ",":
            comma_count += 1

    # iterate through every line after header line
    for line in file_in.readlines():
        # count number of commas
        line_comma_count = 0
        for c in line:
            if c == ",":
                line_comma_count += 1

        # split line
        line_splited = line.split(",")
        # check if there is correct amount of commas and overall_satisfaction cell is not empty
        if line_comma_count == comma_count and (line_splited[satisfaction_index] is not ""):
            # initialize sub list
            sublist = []
            price = float(line_splited[price_index])
            satisfaction = float(line_splited[satisfaction_index])
            if int(line_splited[review_index]) > 0:
                sublist.append(price)
                sublist.append(satisfaction)
                new_list.append(sublist)

    return new_list


def correlation(l):
    """
    This function will return a tuple containing the correlation and pvalue of prices and ratings
    :param l: list - list containing lists of [price, overall_satisfaction]
    :return: tuple - tuple with two elements: correlation and pvalue
    """
    price = []
    rating = []
    for i in l:
        price.append(i[0])
        rating.append(i[1])
    result = spearmanr(price, rating)
    correlation_value = result.correlation
    pvalue = result.pvalue

    t = (correlation_value, pvalue)
    return t


def host_listings(filename):
    """
    Creates and returns a dictionary. The key is host_id and value is a list of room_ids that match the same host_id
    :param filename: string - name of csv file
    :return: dict - dictionary {host_id: [room_ids]}
    """
    hostings = {}
    file_in = open(filename, "r")
    # read the header line and find the index of price, overall_satisfaction, and reviews
    header = file_in.readline()
    header_list = header.split(",")
    host_id_index = header_list.index("host_id")
    room_id_index = header_list.index("room_id")

    for i in file_in.readlines():
        split_string = i.split(",")
        if hostings.get(int(split_string[host_id_index])) is None:
            hostings[int(split_string[host_id_index])] = [int(split_string[room_id_index])]
        else:
            room_ids = hostings.get(int(split_string[host_id_index]))
            room_ids.append(int(split_string[room_id_index]))
            hostings[int(split_string[host_id_index])] = room_ids
    return hostings


def num_listings(dict):
    """
    Function takes a dictionary and returns a list, where list[i] is the number of hosts that have i listings
    :param dict: dict - dictionary of from host_listings
    :return: list - list[i] is the number of hosts that have i listings
    """
    l = []
    num_listings = []
    max_listings = -1
    # append the list size to the num_host list AND find the max number of listings
    for i in dict.values():
        if max_listings < len(i):
            max_listings = len(i)
        num_listings.append(len(i))
    # fill the list, l, with zeros until i is the max_listings + 1
    for i in range(max_listings + 1):
        l.append(0)
    # add 1 to each index of number of listings in num_listings  == index of i
    for i in range(len(l)):
        for k in num_listings:
            if i == k:
                l[i] += 1
    return l


def room_prices(filename_list, roomtype):
    """
    Function returns a dictionary where keys are room_ids and values are lists of price in chronological order
    :param filename_list: list - list of file names
    :param roomtype: string - type of room that can be "Private room", "Shared room", or ""Entire home/apt
    :return:
    """

    # initialize dict function will return
    delta_price = {}
    # sort the files in chronological order
    sorted_files = filename_list[:]
    sorted_files.sort()

    # loop through every file in the list, filename_list
    for filename in sorted_files:
        # open file
        file_in = open(filename, "r")
        header = file_in.readline()
        # find the indexes
        header_list = header.split(",")
        roomtype_index = header_list.index("room_type")
        price_index = header_list.index("price")
        room_id_index = header_list.index("room_id")
        # loop though every line in the file, after header line
        for line in file_in.readlines():
            split_line = line.split(",")
            # check if roomtype is equal to parameter, roomtype
            if split_line[roomtype_index] == roomtype:
                key = int(split_line[room_id_index])
                if delta_price.get(key) is None:
                    delta_price[key] = [float(split_line[price_index])]
                else:
                    prices = delta_price.get(key)
                    prices.append(float(split_line[price_index]))
                    delta_price[key] = prices
    return delta_price


def price_change(dict):
    """
    Returns a tuple that contains the max percentage change, starting price, and ending price
    :param dict: dict - containing key: room_ids and value: list of prices in chronological order
    :return: tuple - (max percentage change, starting price, ending price)
    """
    prices = []
    # copy all the values in dict and append them to a master list
    for i in dict.values():
        prices.append(i)

    # calculate max_percentage_change
    max_percentage_change = ((prices[0][len(prices[0])-1] - prices[0][0])/prices[0][0]) * 100
    starting_price = prices[0][0]
    ending_price = prices[0][len(prices[0])-1]
    t = (max_percentage_change, starting_price, ending_price)
    for i in range(len(prices)):
        # compare previous max_percentage_change to max_percentage_change at index i
        if max_percentage_change < (((prices[i][len(prices[i])-1] - prices[i][0])/prices[i][0]) * 100):
            # update tuple values if there is new max_percentage_change
            max_percentage_change = (((prices[i][len(prices[i])-1] - prices[i][0])/prices[i][0]) * 100)
            starting_price = prices[i][0]
            ending_price = prices[i][len(prices[i])-1]
            t = (max_percentage_change, starting_price, ending_price)
    return t


def main():
    """

    :return:
    """
    file_name = "tomslee_airbnb_brno_1500_2017-07-20.csv"
    # print(price_satisfaction(file_name))
    # print(correlation(price_satisfaction(file_name)))
    # print(host_listings(file_name))
    # print(num_listings(host_listings(file_name)))
    file_list = ["tomslee_airbnb_brno_1258_2017-05-14.csv",
                 "tomslee_airbnb_brno_1500_2017-07-20.csv",
                 "tomslee_airbnb_brno_1383_2017-06-24.csv"]

    file_list2 = ["tomslee_airbnb_los_angeles_1422_2017-07-08.csv",
                 "tomslee_airbnb_los_angeles_0262_2016-01-11.csv",
                 "tomslee_airbnb_los_angeles_0050_2014-09-01.csv"]

    output = room_prices(file_list, "Shared room")
    print(output)
    print(price_change(output))


if __name__ == '__main__':
    main()
