import re

statement1 = open("de.txt").read()
statement2 = """Find all integers $n \geq 3$ for which there exist real numbers $a_1, a_2, \dots a_{n + 2}$ satisfying $a_{n + 1} = a_1$, $a_{n + 2} = a_2$ and
$$a_ia_{i + 1} + 1 = a_{i + 2},$$for $i = 1, 2, \dots, n$.

\textit{Proposed by Patrik Bak, Slovakia}"""
reg1 = re.match("([\s\S]*)\\\\textit\{Proposed by (.*)\}", statement1)
reg2 = re.match("([\s\S]*)\\\\textit\{Proposed by (.*)\}", statement2)
print(reg1)
print(reg2)
print(statement1)
print(statement2)
with open("de1.txt", "w") as f:
    f.write(statement1)
with open("de2.txt", "w") as f:
    f.write(statement2)