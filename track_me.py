import string
import os
import sys
import re
import datetime

import numpy as np
import pandas as pd
from termcolor import colored, cprint
from colorama import Fore, Back, Style

import TrackMeConstant as TmConst


class TrackMe:
    YEAR_INDEX = 0
    MONTH_INDEX = 1
    DAY_INDEX = 2

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __init__(self, body_weight_path):
        self.body_weight_path = body_weight_path
        self.df = pd.read_csv(body_weight_path)

    def read_month(self, month):
        print(self.df[month])
        pass

    def update_body_weight(self, weight, date=None):
        if date is not None:
            raise NotImplementedError('BW: Updating specific date not supported yet.')

        date_today = datetime.date.today()
        date_today = [date_today.year, date_today.month, date_today.day]

        month_ind = date_today[self.MONTH_INDEX]
        month_text = TmConst.MONTH[month_ind - 1]

        day = date_today[self.DAY_INDEX]
        year = date_today[self.YEAR_INDEX]

        print(
            f'Updating body weight for {month_text.capitalize()} {day}, {year}  ...')

        self.df.iat[day-1, month_ind] = weight
        self.df.to_csv(self.body_weight_path, index=False)

        # GREY_SEQ = '\033[38;2;255;100;100m'
        # PAINT_DEFAULT = '\033[K' # A.K.A removing back color erase (bce)

        # print(f"{GREY_SEQ}\033[48;2;0;50;0m"+"123"+"\033[48;2;0;100;0m"+"123"+'\033[32;46m')
        # print(f"{GREY_SEQ}\033[48;2;0;100;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;150;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;200;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;250;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;100;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;150;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;200;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;250;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;100;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;150;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;200;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;250;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;100;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;150;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;200;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;250;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;100;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;150;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;200;0m"+"123")
        # print(f"{GREY_SEQ}\033[48;2;0;250;0m"+"123")

        # print(Fore.RED + 'some red text')
        # print(Back.GREEN + 'and with a green background\ntest')
        # print('\033[41mTest\nTest2\033[0mTest3\033[K')
        # print('\033[41mTest\nTest2\033[0mTest3\033[K')
        # print('test')

        pass

    def print_bw(self):
        print(self.df)
        pass