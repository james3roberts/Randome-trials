import bs4 as bs
import urllib.request
import pandas as pd
import xlsxwriter
from pandas import ExcelWriter
from pandas import ExcelFile
import openpyxl



dfs = pd.read_html('https://www.badgerladder.com/pump-jacks/alum-pump-jack-packages/')
for df in dfs:
    #writer=ExcelWriter('WebScraper.xlsx') 
#df.to_excel(writer,"BadgerLader", index=False)

    print(df)


print('')
print('Poles')
dfs = pd.read_html('https://www.badgerladder.com/aluminum-pump-jack-poles-6-24-long/')
for df in dfs:
    #writer=ExcelWriter('WebScraper.xlsx') 
#df.to_excel(writer,"BadgerLader", index=False)
    print(df)
    pd.concat(dfs, axis=0, join='outer', join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False,
copy=True)

print('')
print('End Rails')
dfs = pd.read_html('https://www.badgerladder.com/aluminum-end-rail-system/')
for df in dfs:
    #writer=ExcelWriter('WebScraper.xlsx') 
###############################################################################################
    df.concat(dfs, axis=0, join='outer', join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False,
copy=True)
###############################################################################################
#df.to_excel(writer,"BadgerLader", index=False)
print(df)
print('')
print('Side Rails')
dfs = pd.read_html('https://www.badgerladder.com/aluminum-side-rail-system/')
for df in dfs:
    print(df)
    pd.concat(dfs, axis=0, join='outer', join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False,
copy=True)
print('')
print('Magnum Tools Page. ')
print('')
print('Guard rails')
sauce = urllib.request.urlopen('https://www.magnumtools.com/products/9890-leader-tool-aluminum-guard-rail-system-grs-00/').read()
soup = bs.BeautifulSoup(sauce,"lxml")
nav= soup.nav
for div in soup.find_all('div', class_= 'col-xs-10'):
   print(div.text)
pd.concat(dfs, axis=0, join='outer', join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False,
copy=True)
print('')
print('End rails')
sauce = urllib.request.urlopen('https://www.magnumtools.com/products/9891-leader-tool-aluminum-end-rail-system-ers-00/').read()
soup = bs.BeautifulSoup(sauce,"lxml")
nav= soup.nav
for div in soup.find_all('div', class_= 'col-xs-10'):
    print(div.text)
    pd.concat(dfs, axis=0, join='outer', join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False,
copy=True)
print('')
print('Packages')
sauce = urllib.request.urlopen('https://www.magnumtools.com/products/7486-magnum-2-pole-48-ft-aluminum-pump-jack-system/').read()
soup = bs.BeautifulSoup(sauce,"lxml")
nav= soup.nav
for div in soup.find_all('div', class_= 'col-xs-10'):
    print(div.text)
pd.concat(dfs, axis=0, join='outer', join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False,
copy=True)
print('')
print('Home Depot. ')
print('')
print('Siding Nails')
sauce = urllib.request.urlopen('https://www.homedepot.com/p/Grip-Rite-2-in-x-0-092-in-15-Wire-Collated-Hot-Galvanized-Ring-Shank-Nails-3-000-Pack-GRC6R90DHG/205865848').read()
soup = bs.BeautifulSoup(sauce,"lxml")
nav= soup.nav
for h1 in soup.find_all('h1', class_= 'product-title__title'):
    print(h1.text)
    sauce = urllib.request.urlopen('https://www.homedepot.com/p/Grip-Rite-2-in-x-0-092-in-15-Wire-Collated-Hot-Galvanized-Ring-Shank-Nails-3-000-Pack-GRC6R90DHG/205865848').read()
    pd.concat(dfs, axis=0, join='outer', join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False,
copy=True)
soup = bs.BeautifulSoup(sauce,"lxml")
nav= soup.nav
for span in soup.find_all('span', class_= 'price__dollars'):
    print(span.text)
    sauce = urllib.request.urlopen('https://www.homedepot.com/p/Freeman-2-in-x-0-092-in-15-Degree-Wire-Collated-Galvanized-Ring-Shank-Coil-Siding-Nails-SNRSG92-2WC/203502710').read()

pd.concat(dfs, axis=0, join='outer', join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False,copy=True)
soup = bs.BeautifulSoup(sauce,"lxml")
nav= soup.nav
for h1 in soup.find_all('h1', class_= 'product-title__title'):
    print(h1.text)
    sauce = urllib.request.urlopen('https://www.homedepot.com/p/Freeman-2-in-x-0-092-in-15-Degree-Wire-Collated-Galvanized-Ring-Shank-Coil-Siding-Nails-SNRSG92-2WC/203502710').read()

    pd.concat(dfs, axis=0, join='outer', join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False,
copy=True)
soup = bs.BeautifulSoup(sauce,"lxml")
nav= soup.nav
for span in soup.find_all('span', class_= 'price__dollars'):
    print(span.text)
    print('Dollars')
sauce = urllib.request.urlopen('https://www.homedepot.com/p/Freeman-2-in-x-0-092-in-Dia-Hot-Dipped-Galvanized-Ring-Shank-Wire-Collated-Siding-Nails-3-600-Count-SNRSHDG92-2WC/301980742').read()

pd.concat(dfs, axis=0, join='outer', join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False,
copy=True)
soup = bs.BeautifulSoup(sauce,"lxml")
nav= soup.nav
for h1 in soup.find_all('h1', class_= 'product-title__title'):
    print(h1.text)
sauce = urllib.request.urlopen('https://www.homedepot.com/p/Freeman-2-in-x-0-092-in-Dia-Hot-Dipped-Galvanized-Ring-Shank-Wire-Collated-Siding-Nails-3-600-Count-SNRSHDG92-2WC/301980742').read()
pd.concat(dfs, axis=0, join='outer', join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False,
copy=True)
soup = bs.BeautifulSoup(sauce,"lxml")
nav= soup.nav
for span in soup.find_all('span', class_= 'price__dollars'):
    print(span.text)
print('////////////////////////Finish////////////////////////////////')
   


# writer.save()
# writer.close()