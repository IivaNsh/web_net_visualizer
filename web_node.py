import os
import requests
from bs4 import BeautifulSoup
import math

def get_links(page):
    links = []
    for link in page.findAll('a'):
        link_text= link.get('href')
        if("https:" in link_text):
            #f.write(link_text+"\n")
            links.append(link_text)
    return links

class web_node:
    def __init__(self, url, base_url, depth):
        self.depth = depth
        self.base_url = base_url
        self.page = requests.get(url)
        self.links = get_links(self.page)
        self.weight_scale = 1
        self.weight = self.weight_scale/(1+math.log(len(self.links+1))) 
        #self.nodes = generate_nodes(self.url, self.depth + 1)
    
