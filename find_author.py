countries = ["Afghanistan","Albania","Algeria","Angola","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahrain","Bangladesh","Belarus","Belgium","Benin","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Cambodia","Canada","Chile","People's Republic of China","China","Colombia","Commonwealth of Independent States","CIS","C.I.S.","Costa Rica","Croatia","Cuba","Cyprus","Czech Republic","Czechoslovakia","Czechia","Denmark","Dominican Republic","Ecuador","Egypt","Estonia","Finland","France","Gambia","Georgia","German Democratic Republic","Germany","Ghana","Greece","Guatemala","Honduras","Hong Kong","HK","H.K.","Hungary","Iceland","India","Indonesia","Iraq","Islamic Republic of Iran","Iran","Ireland","Israel","Italy","Ivory Coast","Jamaica","Japan","Kazakhstan","Kenya","Democratic People's Republic of Korea","North Korea","Republic of Korea","Korea","South Korea","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Liechtenstein","Lithuania","Luxembourg","Macau","Madagascar","Malaysia","Mauritania","Mexico","Republic of Moldova","Moldova","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Nepal","Netherlands","New Zealand","NZ","N.Z.","Nicaragua","Nigeria","North Macedonia","Norway","Oman","Pakistan","Panama","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Romania","Russian Federation","Russia","Rwanda","El Salvador","Saudi Arabia","Senegal","Serbia","Serbia and Montenegro","Singapore","Slovakia","Slovenia","South Africa","Spain","Sri Lanka","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Trinidad and Tobago","Tunisia","Turkey","Turkish Republic of Northern Cyprus","Turkmenistan","Uganda","Ukraine","United Arab Emirates","UAE","U.A.E.","United Kingdom","UK","U.K.","United States of America","United States","USA","US","U.S.A.","U.S.","Uruguay","Union of Soviet Socialist Republics","USSR","U.S.S.R.","Uzbekistan","Venezuela","Vietnam","Yemen","Yugoslavia","Zimbabwe","Scotland","Wales","England"]

statements = []

statements.append("""Prove that there exists a positive constant $c$ such that the following statement is true:
Consider an integer $n > 1$, and a set $\mathcal S$ of $n$ points in the plane such that the distance between any two different points in $\mathcal S$ is at least 1. It follows that there is a line $\ell$ separating $\mathcal S$ such that the distance from any point of $\mathcal S$ to $\ell$ is at least $cn^{-1/3}$.

(A line $\ell$ separates a set of points S if some segment joining two points in $\mathcal S$ crosses $\ell$.)

\textit{Note. Weaker results with $cn^{-1/3}$ replaced by $cn^{-\alpha}$ may be awarded points depending on the value of the constant $\alpha > 1/3$.}
=================================""")

statements.append("""Let $\Gamma$ be the circumcircle of acute triangle $ABC$. Points $D$ and $E$ are on segments $AB$ and $AC$ respectively such that $AD = AE$. The perpendicular bisectors of $BD$ and $CE$ intersect minor arcs $AB$ and $AC$ of $\Gamma$ at points $F$ and $G$ respectively. Prove that lines $DE$ and $FG$ are either parallel or they are the same line.

\textit{Proposed by Silouanos Brazitikos, Evangelos Psychas and Michael Sarantis, Greece}""")

statements.append("""Consider $2018$ pairwise crossing circles no three of which are concurrent. These circles subdivide the plane into regions bounded by circular $edges$ that meet at $vertices$. Notice that there are an even number of vertices on each circle. Given the circle, alternately colour the vertices on that circle red and blue. In doing so for each circle, every vertex is coloured twice- once for each of the two circle that cross at that point. If the two colours agree at a vertex, then it is assigned that colour; otherwise, it becomes yellow. Show that, if some circle contains at least $2061$ yellow points, then the vertices of some region are all yellow.


Proposed by \textit{India}""")

def inc_author(statement=""):
	#1. Last line contains any country name and is less than 120 chars

    #2. Last line is fully italicized and less than 80 chars
    #3. Last line contains "Proposed"
	pass