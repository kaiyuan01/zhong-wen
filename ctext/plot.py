#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# under c9: pip already included; python select v2 or v3
# sudo pip install ctext
# ctext now is installed!

from ctext import *

setlanguage("zh")
setremap("gb")
stats = getstats()

import re
import pandas as pd
import matplotlib.pyplot as plt

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
# %matplotlib inline  

def makevector(string, termlist, normalize = False):
    vector = []
    for term in termlist:
        termcount = len(re.findall(term, string))
        if normalize:
            vector.append(termcount/len(string))
        else:
            vector.append(termcount)
    return vector

text1 = gettextaschapterlist("ctp:fengshen-yanyi")
text2 = gettextaschapterlist("ctp:analects")

vectors1 = []
for chapter in text1:
    vectors1.append(makevector(chapter, ["矣", "也"], True))

vectors2 = []
for chapter in text2:
    vectors2.append(makevector(chapter, ["矣", "也"], True))

df1 = pd.DataFrame(vectors1)
df2 = pd.DataFrame(vectors2)

legend1 = plt.scatter(df1.iloc[:,0], df1.iloc[:,1], color="blue", label="Fengshen Yanyi")
legend2 = plt.scatter(df2.iloc[:,0], df2.iloc[:,1], color="red", label="Analects")
plt.legend(handles = [legend1, legend2])
plt.xlabel("Frequency of 'yi'")
plt.ylabel("Frequency of 'ye'")

