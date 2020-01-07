import bs4 as bs
import urllib.request
import pandas as pd
import xlsxwriter
from pandas import ExcelWriter
from pandas import ExcelFile
import openpyxl
from openpyxl import Workbook
wb=Workbook("WebScraper2.xlsx")
ws = wb.active

dfs = pd.read_html('https://www.badgerladder.com/pump-jacks/alum-pump-jack-packages/')
for df in dfs:
    #writer=ExcelWriter('WebScraper.xlsx') 
    df = ws['A1']
#df.to_excel(writer,"BadgerLader", index=False)

dfs = pd.read_html('https://www.badgerladder.com/aluminum-pump-jack-poles-6-24-long/')
for df in dfs:
    writer=ExcelWriter('WebScraper.xlsx') 
df.to_excel(writer,"BadgerLader", index=False)