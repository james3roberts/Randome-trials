import bs4 as bs
import urllib.request
import pandas as pd 
import xlsxwriter 
from pandas import ExcelWriter
from pandas import ExcelFile
import openpyxl


def one(a):
    dfs = pd.read_html('https://www.badgerladder.com/pump-jacks/alum-pump-jack-packages/')
    for df in dfs:
        print(df)
print(one)