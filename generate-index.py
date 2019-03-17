#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
indexTextStart = """
<!doctype html>
<html>
<head>
	<title>Luck Network | Index of {folderPath}</title>
	<meta charset=\"utf-8\">
	<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">
	<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">
	<meta name=\"description\" content=\"CDN of lucknetwork.jp\">
	<meta name=\"author\" content=\"Luck Network\" />
	<meta content=\"https://cdn.lucknetwork.jp\" property=\"og:url\" />
	<meta content=\"website\" property=\"og:type\" />
	<meta content=\"CDN of lucknetwork.jp\" property=\"og:title\" />
</head>
<body>
    <h2>ディレクトリ {folderPath} 内のファイル</h2>
    <hr>
    <ul>
		<li>
			<a href='../'>../</a>
		</li>
"""
indexTextEnd = """
	</ul>
</body>
</html>
"""

def index_folder(folderPath):
	print("Indexing: " + folderPath +'/')
	#Getting the content of the folder
	files = os.listdir(folderPath)
	#If Root folder, correcting folder name
	root = folderPath
	if folderPath == '.':
		root = 'Root'
	indexText = indexTextStart.format(folderPath=root)
	for file in files:
		#Avoiding index.html files
		if file != 'index.html':
			indexText += "\t\t<li>\n\t\t\t<a href='" + file + "'>" + file + "</a>\n\t\t</li>\n"
		#Recursive call to continue indexing
		if os.path.isdir(folderPath+'/'+file):
			index_folder(folderPath + '/' + file)
	indexText += indexTextEnd
	#Create or override previous index.html
	index = open(folderPath+'/index.html', "w", encoding='utf-8')
	#Save indexed content to file
	index.write(indexText)

#Indexing root directory (Script position)
index_folder('./data')