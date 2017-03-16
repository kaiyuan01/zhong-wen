#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# under c9: pip already included; python select v2 or v3
# sudo pip install ctext
# ctext now is installed!

from ctext import *

setlanguage("zh")
setremap("gb")
stats = getstats()

#print ('ceshi 测试' + str(stats))
# Output: ceshi 测试{'serverlocation': {'description': '服务器所在地', 'value': 'KC'}, 'contribchapters': {'description': '维基区总数（单位）', 'value': '391880'}, 'directquotations': {'description': '直接相同引用', 'value': '3100'}, 'contribchars': {'description': '维基区总字数（汉字）', 'value': '5157143288'}, 'docrespages': {'description': '电子图书馆（页数）', 'value': '25425224'}, 'semanticchars': {'description': '语意链接总字数', 'value': '451466'}, 'paralleltotal': {'description': '相似段落（总数）', 'value': '480270'}, 'chartotal_posthan': {'description': '原典资料库：总字数（汉代之后）', 'value': '20385871'}, 'contribitems': {'description': '维基区总数（原典文献）', 'value': '30392'}, 'semanticcharsp': {'description': '语意链接总字数（%）', 'value': '7.9%'}, 'charfrequpdate': {'description': '汉字几率更新', 'value': None}, 'chartotal': {'description': '原典资料库：总字数（先秦两汉）', 'value': '5687042'}, 'statupdate': {'description': '统计更新', 'value': '2016-10-08 17:37:30'}, 'paragraphtotal': {'description': '总段落', 'value': '85559'}, 'unihan': {'description': 'Unihan数据库版本', 'value': '8.0.0'}, 'parallelgroups': {'description': '相似段落（组数）', 'value': '139634'}

# test paragraph: from: http://digitalsinology.org/classical-chinese-dh-getting-started/

# URN: ctp:analects/xue-er
paragraphs = gettextasparagrapharray("ctp:analects/xue-er")

print("This chapter is made up of " + str(len(paragraphs)) + " paragraphs. These are:")

# For each paragraph of the chapter data that we downloaded, do the following:
for paragraphnumber in range(0, len(paragraphs)):
    print(str(paragraphnumber+1) + ". " + paragraphs[paragraphnumber])
    
    
#output:
#Important: use os.getenv(PORT, 8080) as the port and os.getenv(IP, 0.0.0.0) as the host in your scripts!

#This chapter is made up of 16 paragraphs. These are:
#1. 子曰：「学而时习之，不亦说乎？有朋自远方来，不亦乐乎？人不知而不愠，不亦君子乎？」
#2. 有子曰：「其为人也孝弟，而好犯上者，鲜矣；不好犯上，而好作乱者，未之有也。君子务本，本立而道生。孝弟也者，其为仁之本与！」
# ...
#15. 子贡曰：「贫而无谄，富而无骄，何如？」子曰：「可也。未若贫而乐，富而好礼者也。」子贡曰：「《诗》云：『如切如磋，如琢如磨。』其斯之谓与？」子曰：「赐也 ，始可与言诗已矣！告诸往而知来者。」
#16. 子曰：「不患人之不己知，患不知人也。」
# Process exited with code: 0



########
longest_paragraph = None # We use this variable to record which of the paragraphs we've looked at is longest
longest_length = 0       # We use this one to record how long the longest paragraph we've found so far is

for paragraph_number in range(0, len(paragraphs)):
    paragraph_text = paragraphs[paragraph_number];
    if len(paragraph_text)>longest_length:
        longest_paragraph = paragraph_number
        longest_length = len(paragraph_text)

print("The longest paragraph is paragraph number " + str(longest_paragraph+1) + ", which is " + str(longest_length) + " characters long.")
# Output: The longest paragraph is paragraph number 15, which is 93 characters long.


#############







