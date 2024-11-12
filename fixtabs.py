#!/usr/bin/python3
#
# Turn leading spaces into tabs in a file
# (C) Copyright 2019 Patrick Lambert <patrick@dendory.ca>
# Provided under the MIT License
#

import sys

if len(sys.argv) != 2:
	print("Syntax: fixtabs <text file>")
	exit(1)

try:
	with open(sys.argv[1], "r") as fd:
		data = fd.read()
except:
	print("Error: Could not open {}".format(sys.argv[1]))
	exit(1)

for line in data.split('\n'):
	tcount = 0
	i = 0
	while True:
		if i >= len(line):
			break
		if line[i] == " ":
			i += 1
			tcount += 1
		elif line[i] == "\t":
			i += 1
			tcount += 5
		else:
			break
	if tcount == 0:
		nline = line
	elif tcount < 6:
		nline = "\t{}".format(line.lstrip())
	elif tcount < 11:
		nline = "\t\t{}".format(line.lstrip())
	elif tcount < 16:
		nline = "\t\t\t{}".format(line.lstrip())
	elif tcount < 21:
		nline = "\t\t\t\t{}".format(line.lstrip())
	elif tcount < 26:
		nline = "\t\t\t\t\t{}".format(line.lstrip())
	elif tcount < 31:
		nline = "\t\t\t\t\t\t{}".format(line.lstrip())
	else:
		nline = "\t\t\t\t\t\t\t{}".format(line.lstrip())
	print(nline)
