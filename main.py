import string
import os
import sys
import re
import datetime

import numpy as np
import pandas as pd

import TrackMeConstant as TmConst
from track_me import TrackMe

DATA_PATH = './data/'
WEIGHT_FNAME = 'body_weight_2021.csv'

tm = TrackMe(DATA_PATH + WEIGHT_FNAME)

tm.update_body_weight(189.0)
tm.print_bw()

