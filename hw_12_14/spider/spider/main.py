#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

import bs4
from bs4 import BeautifulSoup
import requests

def getHTML(url):
    '''
        This function get a url and return a
        Beautifulsoup object.'''

    kv = {"user-agent":("User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393")}
    #kv = {"user-agent":"Mozilla/5.0"}
    try:
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "html.parser")
        return soup
    except:
        print("抓取失败!")

def handleHTML(ulist, soup):
    '''
        This function will pick up information from soup.'''

    tbody = soup.find("tbody")
    for tr in tbody.children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])
    return None

def showHTML(ulist, num):
    '''
        This function will show you information that
        you focus on.'''

    mod = "{0:^10}\t\t{1:{3}^10}\t\t{2:^10}"
    print(mod.format("排名", "学校", "城市", chr(12288)))
    for count in range(num):
        print(mod.format(ulist[count][0], ulist[count][1], ulist[count][2], chr(12288)))
    return None

if __name__ == "__main__":
    url = "http://www.zuihaodaxue.cn/shengyuanzhiliangpaiming2017.html"
    ulist = []
    soup = getHTML(url)
    t = soup.find("tbody")
    handleHTML(ulist, soup)
    showHTML(ulist, 20)

