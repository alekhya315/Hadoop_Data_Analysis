#!/usr/bin/env python

import sys
import csv

with sys.stdin as file:
	data = csv.reader(file, delimiter=',')
	data.next()
	for item in data:
		item = filter(None,item[-5:])
		for word in item:
      print(word+"\t"+str(1))
