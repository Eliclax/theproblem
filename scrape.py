from selenium import webdriver
from bs4 import Tag, NavigableString, BeautifulSoup
import pandas as pd

problems=[]
proposers=[]
statement=""

#driver = webdriver.Chrome("/snap/chromium/current/usr/lib/chromium-browser/chromedriver")
#driver.get("https://artofproblemsolving.com/community/c1306546_2020imo")
#content = driver.page_source
#soup = BeautifulSoup(content)

with open("imo2020.html") as imo2020:
    soup = BeautifulSoup(imo2020, 'html.parser')

for a in soup.find_all('div', class_="cmty-view-post-item-text"):
	prob = BeautifulSoup(str(a), 'html.parser')
	statement=""
	#print(list(prob.div.next_elements))
	for desc in prob.div.next_elements:
		if isinstance(desc, NavigableString):
			statement += str(desc)
		elif desc.get('alt') is not None:
			statement += str(desc.get('alt'))
	print(statement)

#df = pd.DataFrame({'Statement':problems,'Proposer':proposers}) 
#df.to_csv('products.csv', index=False, encoding='utf-8')