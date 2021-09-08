from selenium import webdriver
from bs4 import Tag, NavigableString, BeautifulSoup
import pandas as pd
import time
from collections import deque
import random
import re

class Problem:
	def __init__(self, source="", year=-1, label="", statement="", author="", difficulty=-1, rating=-1):
		self.source = source
		self.year = year
		self.label = label
		self.statement = statement
		self.author = author
		self.difficulty = difficulty
		self.rating = rating
	def pretty_print(self):
		stri = "=================================\n"
		stri += "SOURCE: " + self.source + "\n"
		stri += "YEAR: " + str(self.year) + "\n"
		stri += "LABEL: " + self.label + "\n"
		stri += "AUTHOR: " + self.author + "\n"
		stri += "DIFFICULTY: " + str(self.difficulty) + "\n"
		stri += "RATING: " + str(self.rating) + "\n"
		stri += "\n"
		stri += self.statement + "\n"
		return stri
	

problems=[]
linkstack=deque()
namestack=deque()
AOPS = "https://artofproblemsolving.com"
driver = webdriver.Chrome("/snap/chromium/current/usr/lib/chromium-browser/chromedriver")

def html_to_latex(temp_html = ""):
	if temp_html == "":
		print("GOT EMPTY STRING!!")
		return ""

	temp_soup = BeautifulSoup(temp_html, 'html.parser')
	tag = ""
	temp_statement = ""
	
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

	return temp_statement

def aops_dfs(link = ""):
	c=0
	driver.get(link)
	time.sleep(3.5+random.random())
	soup = BeautifulSoup(driver.page_source, 'html.parser')
	source_ = soup.find(class_ = "cmty-category-cell-title").string.rstrip().lstrip()
	print(source_)

	#If page contains folders
	if soup.find(class_ = "cmty-cat-cell-top-legit") is not None:
		for element in soup.find_all(class_ = "cmty-cat-cell-top-legit"):
			aops_dfs(AOPS + str(element.a.get('href')))
	#If page doesn't contain folders, it contains problems. Scrape time.
	else:
		for label_elt in soup.find_all('div', class_="cmty-view-post-item-label"):
			year_ = -1
			if re.match('(?:^|\D)((?:19|20)\d{2})(?:$|\D)', source_).group():
				year_ = re.match('(?:^|\D)((?:19|20)\d{2})(?:$|\D)', source_).group()
			label_ = ""
			if label_elt.string:
				label_ = label_elt.string
			prob_elt = label_elt.find_next(class_="cmty-view-post-item-text")
			author_ = ""
			statement_ = html_to_latex(str(prob_elt))
			reg = re.match("([\s\S]*)\\\\textit\{Proposed by (.*)\}", statement_)
			if reg:
				statement_ = reg.group(1).rstrip()
				author_ = reg.group(2)
			problems.append(Problem(statement=statement_, source=source_, year=year_, author=author_, label=label_))


aops_dfs("https://artofproblemsolving.com/community/c3223_imo_shortlist")
driver.quit()

with open("scrapetest.txt", "w") as f:
	for problem in problems:
		f.write(problem.pretty_print())


df = pd.DataFrame([vars(v) for v in problems])
df.to_csv('scrapetest.csv', index=False, encoding='utf-8')


# for element in soup.find_all(class_ = "cmty-cat-cell-top-legit", limit=2):
# 	linkstack.append(element.a.get('href'))
# 	namestack.append(element.find(class_="cmty-category-cell-title").find(string=True).rstrip().lstrip())

# print(linkstack)
# print(namestack)

# content = driver.page_source
# soup = BeautifulSoup(content, 'html.parser')
# f = open("imo2020_page-source.html", "w")
# f.write(soup.prettify())
# f.close()

#with open("imo2020.html") as imo2020:
#	soup = BeautifulSoup(imo2020, 'html.parser')

#imo2020 = "<i><b>DAY 1</b></i>"
#soup = BeautifulSoup(imo2020, 'html.parser')

# for a in soup.find_all('div', class_="cmty-view-post-item-text"):
# 	statement = html_to_latex(str(a))
# 	print(statement)
# 	problems.append(statement)
