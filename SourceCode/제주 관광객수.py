import urllib.request
import os
import matplotlib as mpl
import sys
import datetime, time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from numpy.random import randn
from matplotlib import font_manager, rc

data=pd.read_csv("./제주특별자치도_국적별관광객현황.csv",encoding="cp949")
print(data)
