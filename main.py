#!/usr/bin/env  python3
import argparse
import numpy as np


def rate(down, mo_payment, term = 24):
    base_value = 26961
    return ((down + term * mo_payment) - base_value) / (base_value - down)


def lin_rate():
    return np.linalg.lstsq([[1, 10000],[1,11000]], [rate(10000, 737),
                                                    rate(11000, 694)])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p",
                        help="Principal",
                        action='store',
                        type=int,
                        default=26961)
    parser.add_argument("-d",
                        help="Down payment",
                        action='store',
                        type=int,
                        default=12000)
    parser.add_argument("-t",
                        help="term",
                        action='store',
                        type=int,
                        default=24)
    parser.add_argument("-m",
                        help="monthly payment",
                        action='store',
                        type=int,
                        default=651)
    parser.add_argument("-r",
                        help="investment rate",
                        action='store',
                        type=float,
                        default=4.9)
    args = parser.parse_args()
    principal = args.p
    down = args.d
    term = args.t
    monthly = args.m
    # rate / 100 is the percentage. This is paid out 4 times a year to 
    # achieve the annualized dividend rate.
    investment_rate = args.r / 400

    invested = term * monthly
    made = 0
    for i in range(term // 3):
        invested -= 3 * monthly
        made += investment_rate * invested
    print(made - (down + monthly * term - principal))


if __name__ == '__main__':
    main()
