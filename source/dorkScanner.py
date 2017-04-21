#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

"""
dorkScanner.py, find sites from dorks.

Usage:
	~$ python2 dorkScanner.py blackvkng 10

	// 10 site will be here about "blackvkng"
"""

__author__ = "Black Viking"
__date__   = "16.04.2017"


import sys
import google

sites = []

def getSites(query, num):
	''' Get sites from query'''

	for site in google.search(query=query, num=int(num), stop=1):
		sites.append("http://"+site.split("/")[2]+"/wp-login.php")

if __name__ == "__main__":
	if len(sys.argv) == 3:
		query = sys.argv[1]
		num   = sys.argv[2]

		getSites(query, num)

		print "\n" + "-"*60
		for site in sites:
			print site
		print "\n" + "-"*60
		print "[+] %s site found!"%(len(sites))

	else:
		sys.exit()
