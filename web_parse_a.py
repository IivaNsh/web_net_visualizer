import os
import requests
from bs4 import BeautifulSoup
import math



all_urls = set()

#web_data struture
#
#[["url1", [1,2]],
# ["url2", [0]],
# ["url3", [0]],]
#
web_data=[]

cr = 0 #used for recursive_parse

def reset_urls():
    all_urls = []

def reset_web_data():
    web_data = []

def reset_all():
    reset_web_data()
    reset_urls()
    cr=0



#gets BeautifulSoup obj an returns set of urls on that page
#maybe not the best way to get urls from web page...
def get_links(page):
    urls = set()
    for line in page.findAll("a"):
        url= line.get("href")
        if url and ("https" in url or "http" in url):
            if not (url in all_urls): 
                # all_urls.add(url) #adding url to set of all urls!
                urls.add(url)
    return urls



#if page cannot be opened returns empty set 
def parse_page_for_urls(url, veiw_page = False):
    urls = set()
    try:
        page = requests.get(url)
        if veiw_page:
            print(page.text)
        bs_page = BeautifulSoup(page.text,"html.parser")
        urls.update(get_links(bs_page)) #adding urls from web page
        return urls
    except:
        return urls



def recursive_parse(base_url, depth=1):
    global cr
    obj = [base_url, []]
    if depth>0:
        urls = set()
        try:
            page = requests.get(base_url)
            bs_page = BeautifulSoup(page.text,"html.parser")
            urls.update(get_links(bs_page)) #adding urls from web page
        except:
            print("-> bad url ->", url)
            web_data.append(obj)
            
        for url in urls:
            n=0
            if not (url in all_urls):
                all_urls.add(url)
                recursive_parse(url, depth=depth-1)
                n=cr
                cr+=1
            else:
                n=[i for i in range(len(web_data)) if web_data[i][0]==url][0]
            obj[1].append(n)

        web_data.append(obj)

    else:
        web_data.append(obj)