import re

countries = ["Afghanistan","Africa","Albania","Algeria","America","Angola","Argentina","Armenia","Asia","Asia-Pacific","Australasia","Australia","Austria","Azerbaijan","Bahrain","Bangladesh","Belarus","Belgium","Benin","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Cambodia","Canada","Chile","China","Colombia","Commonwealth of Independent States","Costa Rica","Croatia","Cuba","Cyprus","Czech Republic","Czechia","Czechoslovakia","Democratic People's Republic of Korea","Denmark","Dominican Republic","Ecuador","Egypt","El Salvador","England","Estonia","Eurafrica","Eurasia","Finland","France","Gambia","Georgia","German Democratic Republic","Germany","Ghana","Greece","Guatemala","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Islamic Republic of Iran","Israel","Italy","Ivory Coast","Jamaica","Japan","Kazakhstan","Kenya","Korea","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Liechtenstein","Lithuania","Luxembourg","Macau","Madagascar","Malaysia","Mauritania","Mexico","Moldova","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Nepal","Netherlands","New Zealand","Nicaragua","Nigeria","North Korea","North Macedonia","Norway","Oceania","Oman","Pakistan","Panama","Paraguay","People's Republic of China","Peru","Philippines","Poland","Portugal","Puerto Rico","Republic of Korea","Republic of Moldova","Romania","Russia","Russian Federation","Rwanda","Saudi Arabia","Scotland","Senegal","Serbia","Serbia and Montenegro","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Trinidad and Tobago","Tunisia","Turkey","Turkish Republic of Northern Cyprus","Turkmenistan","Uganda","Ukraine","Union of Soviet Socialist Republics","United Arab Emirates","United Kingdom","United States","United States of America","Uruguay","Uzbekistan","Venezuela","Vietnam","Wales","Yemen","Yugoslavia","Zimbabwe"]
abbr_countries = ["USSR","U.S.S.R.","USA","US","U.S.A.","U.S.","UK","U.K.","UAE","U.A.E.","NZ","N.Z.","CIS","C.I.S.","H.K.","HK"]

statements = []

# statements.append("""Prove that there exists a positive constant $c$ such that the following statement is true:
# Consider an integer $n > 1$, and a set $\mathcal S$ of $n$ points in the plane such that the distance between any two different points in $\mathcal S$ is at least 1. It follows that there is a line $\ell$ separating $\mathcal S$ such that the distance from any point of $\mathcal S$ to $\ell$ is at least $cn^{-1/3}$.

# (A line $\ell$ separates a set of points S if some segment joining two points in $\mathcal S$ crosses $\ell$.)

# \\textit{Note. Weaker results with $cn^{-1/3}$ replaced by $cn^{-\\alpha}$ may be awarded points depending on the value of the constant $\\alpha > 1/3$.}""")

# statements.append("""Let $\Gamma$ be the circumcircle of acute triangle $ABC$. Points $D$ and $E$ are on segments $AB$ and $AC$ respectively such that $AD = AE$. The perpendicular bisectors of $BD$ and $CE$ intersect minor arcs $AB$ and $AC$ of $\Gamma$ at points $F$ and $G$ respectively. Prove that lines $DE$ and $FG$ are either parallel or they are the same line.

# \\textit{Proposed by Silouanos Brazitikos, Evangelos Psychas and Michael Sarantis, Greece}""")

# statements.append("""Consider $2018$ pairwise crossing circles no three of which are concurrent. These circles subdivide the plane into regions bounded by circular $edges$ that meet at $vertices$. Notice that there are an even number of vertices on each circle. Given the circle, alternately colour the vertices on that circle red and blue. In doing so for each circle, every vertex is coloured twice- once for each of the two circle that cross at that point. If the two colours agree at a vertex, then it is assigned that colour; otherwise, it becomes yellow. Show that, if some circle contains at least $2061$ yellow points, then the vertices of some region are all yellow.


# Proposed by \\textit{India}""")

# statements.append("""Let $R+$ be the set of positive real numbers. Determine all functions $f:R+$ $\rightarrow$ $R+$ such that for all positive real numbers $x$ and $y$
# $f(x+f(xy))+y=f(x)f(y)+1$

# $(Ukraine)$""")

# statements.append("""Find all positive integers $n$ for which there exist non-negative integers $a_1, a_2, \ldots, a_n$ such that
# \[
# \\frac{1}{2^{a_1}} + \\frac{1}{2^{a_2}} + \cdots + \\frac{1}{2^{a_n}} = 
# \\frac{1}{3^{a_1}} + \\frac{2}{3^{a_2}} + \cdots + \\frac{n}{3^{a_n}} = 1.
# \]

# \\textit{Proposed by Dusan Djukic, Serbia}""")

# statements.append("""Let $ABC$ be a triangle with circumcircle $\Omega$ and incentre $I$. Let the line passing through $I$ and perpendicular to $CI$ intersect the segment $BC$ and the arc $BC$ (not containing $A$) of $\Omega$ at points $U$ and $V$ , respectively. Let the line passing through $U$ and parallel to $AI$ intersect $AV$ at $X$, and let the line passing through $V$ and parallel to $AI$ intersect $AB$ at $Y$ . Let $W$ and $Z$ be the midpoints of $AX$ and $BC$, respectively. Prove that if the points $I, X,$ and $Y$ are collinear, then the points $I, W ,$ and $Z$ are also collinear.

# Proposed by David B. Rush, USA""")

textit = "\\textit"
emph = "\\emph"
close_display = "\]"

def split_problem_author(statement=""):
	"""Finds the "last line" of a problem statement."""
	reg = re.match(r"^([\s\S]*\n)(.*)$", statement)
	if reg is None:
		reg = re.match(r"^(.*" + re.escape(close_display) + r")((?!" + re.escape(close_display) + r").*)$", statement)
		if reg is None:
			reg = re.match(r"^(.*\$\$)((?!\$\$).*)$", statement)
			if reg is None:
				return None
		problem_part = reg.group(1)
		author_part = reg.group(2)
	else:
		problem_part = reg.group(1)
		author_part = reg.group(2)
		reg1 = re.match(r"^(.*" + re.escape(close_display) + r")((?!" + re.escape(close_display) + r").*)$", author_part)
		if reg1:
			problem_part += reg1.group(1)
			author_part = reg1.group(2)
		else:
			reg2 = re.match(r"^(.*\$\$)((?!\$\$).*)$", author_part)
			if reg2:
				problem_part += reg2.group(1)
				author_part = reg2.group(2)
	
	return [problem_part.strip(" ()\t\n"), author_part.strip(" ()\t\n")]

def inc_author(statement=""):
	"""Determines whether or not a problem statement includes the author."""
	lines = split_problem_author(statement)
	if lines is None:
		return False
	lastline = lines[1]
	#print("==========================")
	#print("lastline: " + lastline)
	#print("Length: " + str(len(lastline)))

	#1. Last line contains any country name and is less than 130 chars
	if len(lastline) < 130:
		if any(re.match(r".*(?:^|\W)" + re.escape(country) + r"(?:\W|$).*", lastline) for country in countries):
			#print("Matched a country name and <130 chars")
			return True
		if any(re.match(r".*(?:^|\W)" + re.escape(abbr) + r"(?:\W|$).*", lastline) for abbr in abbr_countries):
			#print("Matched a country abbreviation and <130 chars")
			return True

	#2. Last line is fully italicized and less than 100 chars
	if len(lastline) < 100:
		if re.match(r".*\\textit\{.*\}", lastline):
			#print("Matched fully \\textit last line and <100 chars")
			return True
		if re.match(r"\\emph\{.*\}", lastline):
			#print("Matched fully \\emph last line and <100 chars")
			return True
		if re.match(r"(?<!\$)\$(?!\$).*(?<!\$)\$(?!\$)", lastline):
			#print("Matched single dollars signs on last line and <100 chars")
			return True

	#3. Last line contains "Proposed"
	if re.match(r".*Proposed.*", lastline):
		#print("Matched the word \"Proposed\"")
		return True
	return False

def extract_author(statement=""):
	"""Extracts the author"""
	lastline = split_problem_author(statement)[1]

	reg_textit = re.match(r".*" + re.escape(textit) + r"\{(.*)\}", lastline)
	reg_emph = re.match(r".*" + re.escape(emph) + r"\{(.*)\}", lastline)
	reg_dollar_sign = re.match(r"\$(.*)\$", lastline)
	reg_proposed_by = re.match(r".*(?:P|p)roposed by(.*)", lastline)
	reg_proposer = re.match(r".*(?:P|p)roposer(.*)", lastline)
	while reg_textit or reg_emph or reg_dollar_sign or reg_proposed_by or reg_proposer:
		if reg_textit:
			lastline = reg_textit.group(1).strip(" ():\t\n")
		elif reg_emph:
			lastline = reg_emph.group(1).strip(" ():\t\n")
		elif reg_dollar_sign:
			lastline = reg_dollar_sign.group(1).strip(" ():\t\n")
		elif reg_proposed_by:
			lastline = reg_proposed_by.group(1).strip(" ():\t\n")
		elif reg_proposer:
			lastline = reg_proposer.group(1).strip(" ():\t\n")
		reg_textit = re.match(r".*" + re.escape(textit) + r"\{(.*)\}", lastline)
		reg_emph = re.match(r".*" + re.escape(emph) + r"\{(.*)\}", lastline)
		reg_dollar_sign = re.match(r"\$(.*)\$", lastline)
		reg_proposed_by = re.match(r".*(?:P|p)roposed by(.*)", lastline)
		reg_proposer = re.match(r".*(?:P|p)roposer(.*)", lastline)
	
	return lastline
	



for statement_ in statements:
	has_author = inc_author(statement_)
	print("VERDICT: " + str(has_author))
	if has_author:
		print("AUTHOR: " + extract_author(statement_))