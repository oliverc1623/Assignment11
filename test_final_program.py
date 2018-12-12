from final_project import host_listings, price_satisfaction, room_prices, \
    num_listings, correlation, price_change

def main():
    # testing host_listings and num_listings
    d = host_listings("tomslee_airbnb_brno_1500_2017-07-20.csv")
    num_list = num_listings(d)
    print(num_list)
    assert(num_list == [0, 308, 35, 20, 3, 6, 1, 2, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

    # testing price_satisfaction and correlation
    l = price_satisfaction("tomslee_airbnb_brno_1500_2017-07-20.csv")
    correl = correlation(l)
    print(correl)
    assert(correl[0] - .012991413392543557 < 0.0000000001)

    # testing room_prices and max_price_change
    file_list = ["tomslee_airbnb_brno_1258_2017-05-14.csv", \
                 "tomslee_airbnb_brno_1500_2017-07-20.csv", \
                 "tomslee_airbnb_brno_1383_2017-06-24.csv"]
    d = room_prices(file_list, "Shared room")
    price_diff = price_change(d)
    print(price_diff)
    assert(price_diff == (18.75, 16.0, 19.0))


if __name__ == "__main__":
    main()
