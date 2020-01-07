import bs4 as bs
import urllib.request
import pandas as pd


# This will bring up what the source code of what ever web site that you have typed in.///////////////////////////////
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')

# print(soup)

# #This will just print the title.////////////////////////////////////////////////////////
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# print(soup.title)
# #can do print(soup.title.string) This will bring up the title with NO tags involved. 

# #This prints the first paragraph tag./////////////////////////////////////////////////
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# print(soup.p)

# This will find all of the paragraphs on the page//////////////////////////////////////
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# print(soup.find_all('p'))

# The for statement with the .string in the print line gets rid of all of the tags Beware that child tags witll also be removed.//////////////////////////////////////
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# for paragraph in soup.find_all('p'):
#     print(paragraph.string)

# The for statement with the .string in the print line gets rid of all of the tags. Most cases this is the one to use.///////////////////////////////
#sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

# This will bring up all of the text from the entire page reguarless of the tags that are assigned.//////////////////////////////// 
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# print(soup.get_text())

# This will pull all of the links off of the page with the tags. ///////////////////////////////////////////
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# for url in soup.find_all('a'):
#     print(url)

# This will pull all of the links off of the page with no tags. ///////////////////////////////////////////
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# for url in soup.find_all('a'):
#     print(url.get('href'))

############# START OF NAVIGATION //////////////////////////////////////////
#This will find all of the links in the navigation bar across the top. might get more than one list /////////////////////////////
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# nav = soup.nav
# for url in nav.find_all('a'):
#     print(url.get('href'))

## This will pull up th information that has body tags. This should be more than enough if just looking for basic text data///////////////////////
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# body = soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)

#This brings up all of the div tag text. ///////////////////////////////////////
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# nav = soup.nav
# for div in soup.find_all('div'):
#     print(div.text)

# #Thsi will find all the text that is between div tags. /////////////////////////////
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# nav = soup.nav
# for div in soup.find_all('div', class_ = 'body'):
#     print(div.text)

###################### Scraping tables////////////////////////////////////
## tb is table tag. tr is table row tag. th is for table header. td is for table data. //////////////////////////
##This prints off tables and all of the tags. //////////////
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# table = soup.table
# print (table)

# Two ways to look up the tables. ////////////////////////////////////////////////////////////////
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# table = soup.table
# table = soup.find('table')
# # both table = do the same things just different ways to do them. ////////////////////////////////
# print (table)

## finding table rows. using the find_all will find all of the rows insteas do using line 105. that will just find one////////////////
##line 109 gets the table data from the table rows. 
# sauce = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# table = soup.find("table")
# table_rows = table.find_all("tr")
# for tr in table_rows:
#     td=tr.find_all('td')
#     row=[i.text for i in td]
#     print(row)

## Using pandas to get the information out of tables. ///////////////////////////////////
## dfs stands for data frames. 
## pulles the tables from the web page and puts them in a table. /////////////////////////
# dfs = pd.read_html('http://pythonprogramming.net/parsememcparseface/')
# for df in dfs:
#     print(df)

###reading site maps. using the .text and find_all loc "I looked at the tags" brings up just the urls. 
# sauce = urllib.request.urlopen('http://pythonprogramming.net/sitemap.xml').read()
# soup = bs.BeautifulSoup(sauce,'xml')
# for url in soup.find_all('loc'):
#     print(url.text)