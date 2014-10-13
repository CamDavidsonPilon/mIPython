# mipython

import sqlite3
import pandas as pd
import re
from collections import Counter
from pprint import pprint

IPYTHON_HOME = """ipython locate profile""" #run this on your command line

conn = sqlite3.connect('%s/history.sqlite'%IPYTHON_HOME)
cursor = conn.cursor()


def query(q):
    resultset = cursor.execute(q)
    columns = [_[0] for _ in cursor.description]
    return pd.DataFrame( cursor.fetchall(), columns = columns )

def detect_from_import(line):
    regex = """(from|import)\s(\D*?)(\s(import|as).*)?$"""
    v = re.match(regex, line )
    if v:
        return line
    return None

def recommend_imports(df):
    imports = df.apply(detect_from_import)
    top_imports = imports.value_counts().iloc[:5]
    print """We recommend adding the following imports to the startup file '~/.ipython/startup/00-imports.py'"""
    print top_imports.to_string()
    return 


def parse_import(line):
    regex = """(from|import)\s(\D*?)(\s(import|as).*)?$"""
    lines = line.split("\n")
    imports = []
    for line in lines:
        v = re.match(regex, line )
        if v:
            imports.append(v.groups()[1].strip().split(".")[0])
    return imports if imports else None

def parse_assignments(line):
    regex = """\A(\w*)\s?=\s?.*"""
    lines = line.split("\n")
    assignment_variables = []
    for line in lines:
        v = re.match(regex, line )
        if v:
            assignment_variables.append(v.groups()[0].strip())
    return assignment_variables if assignment_variables else None


if __name__=="__main__":
    q = """SELECT source_raw FROM history"""
    df = query(q)['source_raw']

    print "Most common imports:"
    imports = df.apply(parse_import).dropna().sum()
    counter = Counter(imports)
    pprint(counter.most_common(20))

    print
    print "Most common assignemnt variables:"
    ass = df.apply(parse_assignments).dropna().sum()
    counter = Counter(ass)
    pprint(counter.most_common(20))


    print
    recommend_imports(df)




