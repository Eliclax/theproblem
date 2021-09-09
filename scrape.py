from selenium import webdriver
from bs4 import Tag, NavigableString, BeautifulSoup
import pandas as pd
import time
import random
import re
from find_author import inc_author, extract_author, split_problem_author


start_link = "https://artofproblemsolving.com/community/c3414_amc_10"
AOPS = "https://artofproblemsolving.com"
problems=[]


class Problem:
	"""The data structure for Problems."""
	def __init__(self, source="", subtitle="", year=-1, label="", author="", statement="", difficulty=-1, rating=-1, url="", raw=""):
		self.source = source
		self.subtitle = subtitle
		self.year = year
		self.label = label
		self.author = author
		self.statement = statement
		self.difficulty = difficulty
		self.rating = rating
		self.url = url
		self.raw = raw
	def pretty_print(self):
		msg = "=================================\n"
		msg += "SOURCE: " + self.source + "\n"
		msg += "SUBTITLE: " + self.subtitle + "\n"
		msg += "YEAR: " + str(self.year) + "\n"
		msg += "LABEL: " + self.label + "\n"
		msg += "AUTHOR: " + self.author + "\n"
		msg += "DIFFICULTY: " + str(self.difficulty) + "\n"
		msg += "RATING: " + str(self.rating) + "\n"
		msg += "URL: " + self.url + "\n"
		msg += "\n"
		msg += self.statement + "\n"
		return msg

def html_to_latex(temp_html = ""):
	"""From the HTML, get the latex.
	
	Supports italics, bold, enumerate, and itemize."""
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
	"""Recursive depth-first search on AoPS, starting at the given link."""
	driver.get(link)
	folders = 0
	time.sleep(3.5+random.random())
	soup = BeautifulSoup(driver.page_source, 'html.parser')
	folders_now = len(soup.find_all(class_ = "cmty-cat-cell-top-legit"))
	#Keep scrolling down until no new folders appear.
	while folders_now > folders:
		folders = folders_now
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(3.5+random.random())
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		folders_now = len(soup.find_all(class_ = "cmty-cat-cell-top-legit"))
	
	page_title = soup.find(class_ = "cmty-category-cell-title").string.strip()
	print(page_title)
	print("Number of folders found: " + str(folders_now))

	#If page contains folders, continue with DFS.
	if folders > 0:
		for folder in soup.find_all(class_ = "cmty-cat-cell-top-legit"):
			aops_dfs(AOPS + str(folder.a.get('href')))
	#If page doesn't contain folders, it contains problems. Scrape time.
	else:
		print("Scrape Time.")
		labels_since_last_subtitle = 0
		source_ = page_title.strip(" -")
		subtitle_ = ""
		year_ = -1
		url_ = driver.current_url
		if re.match('(?:^|\D)((?:19|20)\d{2})(?:$|\D)', source_).group():
			year_ = re.match('(?:^|\D)((?:19|20)\d{2})(?:$|\D)', source_).group(1)
		#For each item on the page
		for item in soup.find_all('div', class_="cmty-view-posts-item"):
			print("Item found")
			author_ = ""
			label_ = ""
			#Find item's label.
			if item.find(class_="cmty-view-post-item-label"):
				print("label found")
				label_elt = item.find(class_="cmty-view-post-item-label")
				if label_elt.string:
					label_ = label_elt.string
			#No label? We're in a subtitle. Get subtitlem overwrite/append, and continue.
			elif labels_since_last_subtitle == 0:
				print("No label found. Continued subtitle found")
				if subtitle_ != "" and item.find(class_="cmty-view-post-item-text").string:
					subtitle_ += " -- " + item.find(class_="cmty-view-post-item-text").string
				elif item.find(class_="cmty-view-post-item-text").string:
					subtitle_ = item.find(class_="cmty-view-post-item-text").string
				continue
			else:
				print("No label found. New subtitle found")
				if item.find(class_="cmty-view-post-item-text").string:
					subtitle_ = item.find(class_="cmty-view-post-item-text").string
				labels_since_last_subtitle = 0
				continue
			#If the label is empty, the item is probably not a problem. Skip item.
			if label_ == "":
				print("Label is Empty")
				continue
			#Our item has a populated label. Woohoo!
			labels_since_last_subtitle += 1

			prob_elt = label_elt.find_next(class_="cmty-view-post-item-text")
			statement_ = html_to_latex(str(prob_elt)).strip()
			raw_ = statement_
			has_author = inc_author(statement_)
			if has_author:
				author_ = extract_author(statement_)
				statement_ = split_problem_author(statement_)[0]
			problems.append(Problem(source_, subtitle_, year_, label_, author_, statement_, -1, -1, url_, raw_))

driver = webdriver.Chrome("/snap/chromium/current/usr/lib/chromium-browser/chromedriver")
aops_dfs(start_link)
driver.quit()

# with open("scrape.txt", "w") as f:
# 	for problem in problems:
# 		f.write(problem.pretty_print())

#make scrape.csv
df = pd.DataFrame([vars(v) for v in problems])
df.to_csv('scrape.csv', sep='|' ,index=False, encoding='utf-8')


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
