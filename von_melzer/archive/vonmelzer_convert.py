import re
import sys
from collections import Counter
import pandas as pd

print(sys.argv)

def align_page(page):
    ends = sum([[m.end() for m in re.finditer(' {5,}', ln)] for ln in page], [])
    ends = [e for e in ends if e > 25]
    most = sorted([k for k, c in Counter(ends).most_common(4) if c > 1])
    if len(most) < 3:
        print(page)
    if len(most) == 3:
        most = [most[0], most[1], most[2], most[2]]
    return [5] + most

def line_grouper(inp):
    group = None
    for ln in inp:
        if ln[0].isnumeric():
            if group is not None:
                yield group
            group = [ln]
        else:
            group += [ln]

def page_grouper(inp):
    group = None
    skip = 0
    for ln in inp:
        if skip > 0:
            skip -= 1
            continue
        if ln.startswith('\u000c'):
            if group is not None:
                yield group
            group = []
            skip = 1
        else:
            group += [ln]

def parse_line(ln, part):
    return (
        ln[:part[0]].strip(),
        ln[part[0]:part[1]].strip(),
        ln[part[1]:part[2]].strip(),
        ln[part[2]:part[3]].strip(),
        ln[part[3]:part[4]].strip(),
        ln[part[4]:].strip()
    )

def parse_page(page):
    lines = [x for x in page[1:] if len(x.strip()) > 0 or x.strip().isnumeric()]
    mlines = [(ln if ln[:5].strip().isnumeric() else '  '+ln) for ln in lines]
    align = align_page(mlines)
    plines = [parse_line(ln, align) for ln in mlines]
    return plines

doc = open(sys.argv[1]).read()

lines = doc.split('\n')
pages = list(page_grouper(lines))
alines = sum([parse_page(pg) for pg in pages], [])

pgroup = list(line_grouper(alines))
tgroup = [[' '.join(x).strip() for x in zip(*grp)] for grp in pgroup]

colnames = ['Persisch', 'Präs.-Stamm', 'Transkription', 'Deutsch', 'Bemerkung', 'Quellenangaben']
dftot = pd.DataFrame(tgroup, columns=colnames)
print(len(dftot))

dftot.to_excel(sys.argv[2])
