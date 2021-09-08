from selenium import webdriver
from bs4 import Tag, NavigableString, BeautifulSoup
import pandas as pd

problems=[]
proposers=[]
statement=""
c=0

#driver = webdriver.Chrome("/snap/chromium/current/usr/lib/chromium-browser/chromedriver")
#driver.get("https://artofproblemsolving.com/community/c1306546_2020imo")
#content = driver.page_source
#soup = BeautifulSoup(content)


with open("imo2020.html") as imo2020:
	soup = BeautifulSoup(imo2020, 'html.parser')

#imo2020 = "<i><b>DAY 1</b></i>"
#soup = BeautifulSoup(imo2020, 'html.parser')

def html_to_latex(temp_html = ""):
	#print("===========================")
	if temp_html == "":
		print("GOT EMPTY STRING!!")
		return ""

	temp_soup = BeautifulSoup(temp_html, 'html.parser')
	tag = ""
	temp_statement = ""

	# print("temp_soup: ")
	# print(str(temp_soup))
	# print("temp_soup.find(): ")
	# print(str(temp_soup.find()))
	# print("type(temp_soup.find()): ")
	# print(type(temp_soup.find()))
	# print("temp_soup.find(string=True): ")
	# print(str(temp_soup.find(string=True)))
	# print("type(temp_soup.find(string=True)): ")
	# print(type(temp_soup.find(string=True)))

	
	if isinstance(temp_soup.find(), Tag):
		tag = temp_soup.find().name
		if temp_soup.find().name == 'img':
			temp_statement += temp_soup.find().get('alt')
		for b in temp_soup.find().children:
			#print("b: ", str(b))
			temp_statement += html_to_latex(str(b))
	else:
		temp_statement += temp_soup.find(string=True)
		
	if tag == "i":
		temp_statement = '\\textit{' + temp_statement + '}'
	elif tag == "b":
		temp_statement = '\\textbf{' + temp_statement + '}'
	elif tag == "ul":
		temp_statement = '\\begin{itemize}' + temp_statement + '\\end{itemize}'
	elif tag == "ol":
		temp_statement = '\\begin{enumerate}' + temp_statement + '\\end{enumerate}'
	elif tag == "li":
		temp_statement = '\\item ' + temp_statement

	#print(temp_statement)
	return temp_statement

#problems.append(html_to_latex(str(soup)))
#print(problems)

for a in soup.find_all('div', class_="cmty-view-post-item-text"):
	statement = html_to_latex(str(a))
	print(statement)
	problems.append(statement)

#print(problems[3])




	# prob = BeautifulSoup(str(a), 'html.parser')
	# statement = ""
	# for desc in prob.div.next_elements:
	# 	print(desc)
	# 	if isinstance(desc, NavigableString):
	# 		statement += str(desc)
	# 	elif desc.get('alt') is not None:
	# 		statement += str(desc.get('alt'))
	# print(statement)

df = pd.DataFrame({'Statement':problems}) 
df.to_csv('imo2020.csv', index=False, encoding='utf-8')